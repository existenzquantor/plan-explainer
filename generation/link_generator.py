from typing import List, Set, Tuple
from classes import Operator, Fact

def test_precondition(pre: Set[Fact], state: Set[Fact]) -> bool:
    return pre.issubset(state)

def has_effect(fact: Fact, eff: Set[Fact]) -> bool:
    return fact in eff

def has_precondition(fact: Fact, pre: Set[Fact]) -> bool:
    return fact in pre

def is_applicable(action: Operator, state: Set[Fact]) -> bool:
    return test_precondition(action.pre, state)

def apply_effects(eff: Set[Fact], state: Set[Fact]) -> Set[Fact]:
    neg = get_fact_negations(eff)
    state = state.difference(neg)
    state = state.union(eff)
    return state

def get_fact_negations(facts: Set[Fact]) -> Set[Fact]:
    res = set()
    for f in facts:
        res.add(Fact(f.name, not f.value))
    return res

def apply_action(action: Operator, state: Set[Fact]) -> Set[Fact]:
    return apply_effects(action.eff, state)

def apply_plan(plan: List[Operator], state: Set[Fact]) -> Set[Fact]:
    state = state.copy()
    for a in plan:
        if not is_applicable(a, state):
            raise Exception(f"{a} is not applicable in {state}")
        state = apply_action(a, state)
    return state

def reaches_goal(plan: List[Operator], init: Set[Fact], goal: Set[Fact]) -> bool:
    try:
        state = apply_plan(plan, init)
        return test_precondition(goal, state)
    except:
        return False

def subsequent_plan_exists(plan: List[Operator], init: Set[Fact], goal: Set[Fact]):
    if reaches_goal(plan, init, goal):
        return True
    if len(plan) > 0:
        for i in range(len(plan)):
            new_plan = plan.copy()
            del new_plan[i]
            if subsequent_plan_exists(new_plan.copy(), init, goal):
                return True
    return False

def is_demander(v: Fact, t: int, Plan: List[Operator], init: Set[Fact], goal: Set[Fact]) -> bool:
    new_init = init.copy()
    new_init = apply_plan(Plan[0 : t], init)
    if not has_precondition(v, new_init):
        return False
    new_init.remove(v)
    new_init.add(negation_of(v))
    return subsequent_plan_exists(Plan[t+1:len(Plan)], new_init, goal)

def negation_of(v: Fact) -> Fact:
    return Fact(v.name, not v.value)

def get_producers(v: Fact, t: int, Plan: List[Operator], state: Set[Fact]) -> List[Tuple[str, int]]:
    producers = []
    if t == 0 and has_effect(v, state):
        producers.append(["Init", -1])
    else:
        ix = list(range(0,t))
        ix.reverse()
        negated = False
        for i in ix:
            if has_effect(negation_of(v), Plan[i].eff):
                negated = True
            if not negated and has_effect(v, Plan[i].eff):
                producers.append([Plan[i].name, i])
        if not negated and has_effect(v, state):
            producers.append(["Init", -1])
    return producers

def get_all_d_links(state: Set[Fact], Plan: List[Operator], goal: Set[Fact]) -> List:
    d_links = []
    for v in state:
        for t in range(len(Plan)):
            if is_demander(v, t, Plan, state, goal):
                producers = get_producers(v, t, Plan, state)
                for p in producers:
                    next_action = Plan[t].name if t < len(Plan) else "Goal"
                    d_links.append([p, v, t, next_action])
            if is_demander(negation_of(v), t, Plan, state, goal):
                producers = get_producers(negation_of(v), t, Plan, state)
                for p in producers:
                    next_action = Plan[t].name if t < len(Plan) else "Goal"
                    d_links.append([p, negation_of(v), t, next_action])
    for i in range(len(d_links)):
        d_links[i] = [d_links[i][0][1], d_links[i][0][0], d_links[i][1].__repr__(), d_links[i][2], d_links[i][3]]
    return d_links

def get_all_standard_links(state: Set[Fact], Plan: List[Operator], goal: Set[Fact]) -> List:
    e_links = []
    for v in state:
        for t in range(len(Plan)+1):
            if (t == len(Plan) and has_precondition(v, goal)) or (t < len(Plan) and has_precondition(v, Plan[t].pre)):
                producers = get_producers(v, t, Plan, state)
                for p in producers:
                    next_action = Plan[t].name if t < len(Plan) else "Goal"
                    e_links.append([p, v, t, next_action])
            if (t == len(Plan) and has_precondition(negation_of(v), goal)) or (t < len(Plan) and has_precondition(negation_of(v), Plan[t].pre)):
                producers = get_producers(negation_of(v), t, Plan, state)
                for p in producers:
                    next_action = Plan[t].name if t < len(Plan) else "Goal"
                    e_links.append([p, negation_of(v), t, next_action])
    for i in range(len(e_links)):
        e_links[i] = [e_links[i][0][1], e_links[i][0][0], e_links[i][1].__repr__(), e_links[i][2], e_links[i][3]]
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