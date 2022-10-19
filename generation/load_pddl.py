import pddl_parser.PDDL as pddl

def make_name(name, args):
    name = "(" + name + " "
    for a in args:
        name = name + a + " "
    name = name[0:-1] + ")"
    return name

def ground_actions(parser):
    ground_actions = []
    for action in parser.actions:
        for act in action.groundify(parser.objects, parser.types):
            ground_actions.append(act)
    return ground_actions

def load_domain_problem(name):
    parser = pddl.PDDL_Parser()
    parser.parse_domain("./pddl/"+name+"_domain.pddl")
    parser.parse_problem("./pddl/"+name+"_problem.pddl")

    # Collect all possible facts and operators
    fact_names = set()
    init_facts = []

    # Initial state
    for f in parser.state:
        init_facts.append(make_name(f[0], f[1:]))
        fact_names.add(make_name(f[0], f[1:]))
    
    # Grounded domain
    grounded = ground_actions(parser)

    my_operators = []

    for go in grounded:

        opname = make_name(go.name, [v for v in go.parameters])

        god = {"name": opname, "pre": dict(), "eff": dict()}

        for i in go.positive_preconditions:
            n = make_name(i[0], i[1:])
            god["pre"][n] = True
            fact_names.add(n)
        for i in go.negative_preconditions:
            n = make_name(i[0], i[1:])
            god["pre"][n] = False
            fact_names.add(n)
        for i in go.add_effects:
            n = make_name(i[0], i[1:])
            god["eff"][n] = True
            fact_names.add(n) 
        for i in go.del_effects:
            n = make_name(i[0], i[1:])
            god["eff"][n] = False
            fact_names.add(n)

        my_operators.append(god)

    # Build goal description
    goal = {}
    for f in parser.positive_goals:
        n = make_name(f[0], f[1:])
        goal[n] = True
        fact_names.add(n)
    for f in parser.negative_goals:
        n = make_name(f[0], f[1:])
        goal[n] = False
        fact_names.add(n)

    # Build init state
    init = {}
    for f in fact_names:
        if f in init_facts:
            init[f] = True
        else:
            init[f] = False

    return init, goal, my_operators


