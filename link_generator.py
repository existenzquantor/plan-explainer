
import sys

def testPrecondition(pre, state):
    for k, v in pre.items():
        if state[k] != v:
            return False
    return True

def hasEffect(fact, eff):
    if list(fact.keys())[0] in list(eff.keys()) and eff[list(fact.keys())[0]] == fact[list(fact.keys())[0]]:
        return True
    return False

def hasPrecondition(fact, pre):
    if list(fact.keys())[0] in list(pre.keys()) and pre[list(fact.keys())[0]] == fact[list(fact.keys())[0]]:
        return True
    return False

def isApplicable(action, state):
    return testPrecondition(action["pre"], state)

def applyEffects(eff, state):
    state = state.copy()
    for k, v in eff.items():
        state[k] = v
    return state

def applyAction(action, state):
    state = state.copy()
    return applyEffects(action["eff"], state)

def applyPlan(plan, state):
    state = state.copy()
    for a in plan:
        if not isApplicable(a, state):
            return False
        state = applyAction(a, state)
    return state

def reachesGoal(plan, init, goal):
    state = applyPlan(plan, init)
    if state:
        return testPrecondition(goal, state)
    return False

def subsequentPlanExists(plan, init, goal):
    if reachesGoal(plan, init, goal):
        #for a in plan:
        #    print(a["name"])
        #print(init)
        return True
    if len(plan) > 0:
        for i in range(len(plan)):
            newPlan = plan.copy()
            del newPlan[i]
            if subsequentPlanExists(newPlan.copy(), init, goal):
                return True
    return False

def isDemander(v, t, Plan, init, goal):
    newInit = dict()
    newInit = applyPlan(Plan[0 : t], init)
    if not testPrecondition(v, newInit):
        return False
    newInit[list(v.keys())[0]] = not v[list(v.keys())[0]]
    #print(init, v, newInit)
    return subsequentPlanExists(Plan[t+1:len(Plan)], newInit, goal)

def negationOf(v):
    k, v = list(v.items())[0]
    return {k : not v}

def getProducers(v, t, Plan, state):
    producers = []
    if t == 0 and hasEffect(v, state):
        producers.append(["Init", -1])
    else:
        ix = list(range(0,t))
        ix.reverse()
        negated = False
        for i in ix:
            if hasEffect(negationOf(v), Plan[i]["eff"]):
                negated = True
            if not negated and hasEffect(v, Plan[i]["eff"]):
                producers.append([Plan[i]["name"], i])
        if not negated and hasEffect(v, state):
            producers.append(["Init", -1])
    return producers

def getAllDLinks(state, Plan, goal):
    gLinks = []
    for k, v in state.items():
        for t in range(len(Plan)):
            if isDemander({k:v}, t, Plan, state, goal):
                producers = getProducers({k:v}, t, Plan, state)
                for p in producers:
                    nextAction = Plan[t]["name"] if t < len(Plan) else "Goal"
                    gLinks.append([p, {k:v}, t, nextAction])
            if isDemander({k:not v}, t, Plan, state, goal):
                producers = getProducers({k:not v}, t, Plan, state)
                for p in producers:
                    nextAction = Plan[t]["name"] if t < len(Plan) else "Goal"
                    gLinks.append([p, {k:not v}, t, nextAction])
    return gLinks

def getAllELinks(state, Plan, goal):
    eLinks = []
    for k, v in state.items():
        for t in range(len(Plan)+1):
            if (t == len(Plan) and hasPrecondition({k:v}, goal)) or (t < len(Plan) and hasPrecondition({k:v}, Plan[t]["pre"])):
                producers = getProducers({k:v}, t, Plan, state)
                for p in producers:
                    nextAction = Plan[t]["name"] if t < len(Plan) else "Goal"
                    eLinks.append([p, {k: v}, t, nextAction])
            if (t == len(Plan) and hasPrecondition({k:not v}, goal)) or (t < len(Plan) and hasPrecondition({k:not v}, Plan[t]["pre"])):
                producers = getProducers({k:not v}, t, Plan, state)
                for p in producers:
                    nextAction = Plan[t]["name"] if t < len(Plan) else "Goal"
                    eLinks.append([p, {k: not v}, t, nextAction])
    return eLinks





if __name__ == "__main__":
    print(sys.argv[1])
    my = __import__(sys.argv[1])

    print("D-LINKS")
    dLinks = getAllDLinks(my.init, my.Plan, my.goal)
    for d in dLinks:
        print(d)


    print("E-LINKS")
    eLinks = [x for x in getAllELinks(my.init, my.Plan, my.goal) if x not in dLinks]
    for e in eLinks:
        print(e)


    # Verbalization
    for e in eLinks:
        pass