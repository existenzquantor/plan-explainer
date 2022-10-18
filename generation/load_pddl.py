from pddlpy import DomainProblem

def make_name(name, args):
    name = "(" + name + " "
    for a in args:
        name = name + a + " "
    name = name[0:-1] + ")"
    return name

def load_domain_problem(name):
    domprob = DomainProblem("./pddl/"+name+"_domain.pddl", "./pddl/"+name+"_problem.pddl")

    # Collect all possible facts and operators
    fact_names = []
    init_facts = []

    for f in domprob.initialstate():
        fact_names.append(make_name(f.predicate[0], f.predicate[1:]))
        init_facts.append(make_name(f.predicate[0], f.predicate[1:]))

    my_operators = []

    op = domprob.operators()
    for o in op:
        for go in domprob.ground_operator(o):

            opname = make_name(go.operator_name, [v for v in go.variable_list.values()])

            god = {"name": opname, "pre": dict(), "eff": dict()}

            for i in go.precondition_pos:
                if not i[0] in fact_names:
                    god["pre"][make_name(i[0], i[1:])] = True
                    fact_names.append(make_name(i[0], i[1:]))
            for i in go.precondition_neg:
                if not i[0] in fact_names:
                    god["pre"][make_name(i[0], i[1:])] = False
                    fact_names.append(make_name(i[0], i[1:]))
            for i in go.effect_pos:
                if not i[0] in fact_names:
                    god["eff"][make_name(i[0], i[1:])] = True
                    fact_names.append(make_name(i[0], i[1:]))
            for i in go.effect_neg:
                if not i[0] in fact_names:
                    god["eff"][make_name(i[0], i[1:])] = False
                    fact_names.append(make_name(i[0], i[1:]))
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
        goal[make_name(f.predicate[0], f.predicate[1:])] = True

    return init, goal, my_operators


