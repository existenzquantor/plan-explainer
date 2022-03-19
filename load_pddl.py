from pddlpy import DomainProblem

def make_name(name, args, truth = None):
    name = "(" + name + " "
    for a in args:
        name = name + a + " "
    name = name[0:-1] + ")"
    #if truth == False:
    #    name = "(not " + name + ")"
    return name

def loadDomainProblem(name):
    domprob = DomainProblem("./pddl/"+name+"_domain.pddl", "./pddl/"+name+"_problem.pddl")

    # Collect all possible facts and operators
    fact_names = []
    init_facts = []

    for f in domprob.initialstate():
        fact_names.append(make_name(f.predicate[0], f.predicate[1:], True))
        init_facts.append(make_name(f.predicate[0], f.predicate[1:], True))

    my_operators = []

    op = domprob.operators()
    for o in op:
        for go in domprob.ground_operator(o):

            opname = make_name(go.operator_name, [v for v in go.variable_list.values()])

            god = {"name": opname, "pre": dict(), "eff": dict()}

            for i in go.precondition_pos:
                if not i[0] in fact_names:
                    god["pre"][make_name(i[0], i[1:], True)] = True
                    fact_names.append(make_name(i[0], i[1:], True))
            for i in go.precondition_neg:
                if not i[0] in fact_names:
                    god["pre"][make_name(i[0], i[1:], False)] = False
                    fact_names.append(make_name(i[0], i[1:], False))
            for i in go.effect_pos:
                if not i[0] in fact_names:
                    god["eff"][make_name(i[0], i[1:], True)] = True
                    fact_names.append(make_name(i[0], i[1:], True))
            for i in go.effect_neg:
                if not i[0] in fact_names:
                    god["eff"][make_name(i[0], i[1:], False)] = False
                    fact_names.append(make_name(i[0], i[1:], True))
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
        goal[make_name(f.predicate[0], f.predicate[1:], True)] = True

    print(init, goal, my_operators)
    return init, goal, my_operators


