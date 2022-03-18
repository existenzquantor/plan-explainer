from pddlpy import *

def loadDomainProblem(name):
    domprob = DomainProblem("./pddl/"+name+"_domain.pddl", "./pddl/"+name+"_problem.pddl")

    # Collect all possible facts and operators
    fact_names = []
    init_facts = []

    for f in domprob.initialstate():
        fact_names.append(f.predicate[0]+""+f.predicate[1])
        init_facts.append(f.predicate[0]+""+f.predicate[1])

    my_operators = []

    op = domprob.operators()
    for o in op:
        for go in domprob.ground_operator(o):

            god = {"name": go.operator_name, "pre": dict(), "eff": dict()}

            for i in go.precondition_pos:
                if not i[0] in fact_names:
                    god["pre"][i[0]+""+i[1]] = True
                    fact_names.append(i[0]+""+i[1])
            for i in go.precondition_neg:
                if not i[0] in fact_names:
                    god["pre"][i[0]+""+i[1]] = False
                    fact_names.append(i[0]+""+i[1])
            for i in go.effect_pos:
                if not i[0] in fact_names:
                    god["eff"][i[0]+""+i[1]] = True
                    fact_names.append(i[0]+""+i[1])
            for i in go.effect_neg:
                if not i[0] in fact_names:
                    god["eff"][i[0]+""+i[1]] = False
                    fact_names.append(i[0]+""+i[1])

            my_operators.append(god)


    # Build init state
    init = {}
    for f in fact_names:
        if f in init_facts:
            init[f] = True
        else:
            init[f] = False


    # Build goal description
    goal = {}
    for f in domprob.goals():
        goal[f.predicate[0]+""+f.predicate[1]] = True

    return init, goal, my_operators


