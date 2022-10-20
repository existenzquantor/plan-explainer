def test_precondition(pre, state):
    for k, v in pre.items():
        if state[k] != v:
            return False
    return True

def has_effect(fact, eff):
    name = list(fact.keys())[0]
    if name in list(eff.keys()) and eff[name] == fact[name]:
        return True
    return False

def has_precondition(fact, pre):
    name = list(fact.keys())[0]
    if name in list(pre.keys()) and pre[name] == fact[name]:
        return True
    return False

def is_applicable(action, state):
    return test_precondition(action["pre"], state)

def apply_effects(eff, state):
    state = state.copy()
    for k, v in eff.items():
        state[k] = v
    return state

def apply_action(action, state):
    state = state.copy()
    return apply_effects(action["eff"], state)

def apply_plan(plan, state):
    state = state.copy()
    for a in plan:
        if not is_applicable(a, state):
            return False
        state = apply_action(a, state)
    return state

def reaches_goal(plan, init, goal):
    state = apply_plan(plan, init)
    if state:
        return test_precondition(goal, state)
    return False

def subsequent_plan_exists(plan, init, goal):
    if reaches_goal(plan, init, goal):
        return True
    if len(plan) > 0:
        for i in range(len(plan)):
            new_plan = plan.copy()
            del new_plan[i]
            if subsequent_plan_exists(new_plan.copy(), init, goal):
                return True
    return False

def is_demander(v, t, Plan, init, goal):
    new_init = dict()
    new_init = apply_plan(Plan[0 : t], init)
    if not test_precondition(v, new_init):
        return False
    name = list(v.keys())[0]
    new_init[name] = not v[name]
    return subsequent_plan_exists(Plan[t+1:len(Plan)], new_init, goal)

def negation_of(v):
    k, v = list(v.items())[0]
    return {k : not v}

def get_producers(v, t, Plan, state):
    producers = []
    if t == 0 and has_effect(v, state):
        producers.append(["Init", -1])
    else:
        ix = list(range(0,t))
        ix.reverse()
        negated = False
        for i in ix:
            if has_effect(negation_of(v), Plan[i]["eff"]):
                negated = True
            if not negated and has_effect(v, Plan[i]["eff"]):
                producers.append([Plan[i]["name"], i])
        if not negated and has_effect(v, state):
            producers.append(["Init", -1])
    return producers

def get_all_d_links(state, Plan, goal):
    d_links = []
    for k, v in state.items():
        for t in range(len(Plan)):
            if is_demander({k:v}, t, Plan, state, goal):
                producers = get_producers({k:v}, t, Plan, state)
                for p in producers:
                    next_action = Plan[t]["name"] if t < len(Plan) else "Goal"
                    d_links.append([p, {k:v}, t, next_action])
            if is_demander({k:not v}, t, Plan, state, goal):
                producers = get_producers({k:not v}, t, Plan, state)
                for p in producers:
                    next_action = Plan[t]["name"] if t < len(Plan) else "Goal"
                    d_links.append([p, {k:not v}, t, next_action])
    for i in range(len(d_links)):
        d_links[i] = [d_links[i][0][1], d_links[i][0][0], d_links[i][1], d_links[i][2], d_links[i][3]]
    return d_links

def get_all_standard_links(state, Plan, goal):
    e_links = []
    for k, v in state.items():
        for t in range(len(Plan)+1):
            if (t == len(Plan) and has_precondition({k:v}, goal)) or (t < len(Plan) and has_precondition({k:v}, Plan[t]["pre"])):
                producers = get_producers({k:v}, t, Plan, state)
                for p in producers:
                    next_action = Plan[t]["name"] if t < len(Plan) else "Goal"
                    e_links.append([p, {k: v}, t, next_action])
            if (t == len(Plan) and has_precondition({k:not v}, goal)) or (t < len(Plan) and has_precondition({k:not v}, Plan[t]["pre"])):
                producers = get_producers({k:not v}, t, Plan, state)
                for p in producers:
                    next_action = Plan[t]["name"] if t < len(Plan) else "Goal"
                    e_links.append([p, {k: not v}, t, next_action])
    for i in range(len(e_links)):
        e_links[i] = [e_links[i][0][1], e_links[i][0][0], e_links[i][1], e_links[i][2], e_links[i][3]]
    return e_links

def get_all_links(init, Plan, goal):
    d_links = get_all_d_links(init, Plan, goal)
    e_links = [x for x in get_all_standard_links(init, Plan, goal) if x not in d_links]
    return e_links, d_links

def generate_explanations(init, plan, goal):
    e_links, d_links = get_all_links(init, plan, goal)
    d_links = sorted(d_links, key=lambda x: (x[3], x[0]) )
    e_links = sorted(e_links, key=lambda x: (x[3], x[0]) )

    return e_links, d_links