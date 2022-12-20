import sys
from typing import Sequence, List
import pddl_parser.PDDL as pddl
from classes import Operator, Fact

def make_name(name: str, args: Sequence) -> str:
    return " ".join([name, *args])

def make_plan(operators: List[Operator]) -> List[Operator]:
    plan = []
    for a in sys.argv[2].split(";"):
        for o in operators:
            if o.name == a.lower():
                plan.append(o)
                break
    return plan

def ground_actions(parser):
    ground_actions = []
    for action in parser.actions:
        for act in action.groundify(parser.objects, parser.types):
            ground_actions.append(act)
    return ground_actions

def load_domain_problem(name: str):
    parser = pddl.PDDL_Parser()
    parser.parse_domain("./pddl/"+name+"_domain.pddl")
    parser.parse_problem("./pddl/"+name+"_problem.pddl")

    # Collect all possible facts and operators
    fact_names = set()
    init_facts = set()

    # Initial state
    for f in parser.state:
        init_facts.add(make_name(f[0], f[1:]))
        fact_names.add(make_name(f[0], f[1:]))
    
    # Grounded domain
    grounded = ground_actions(parser)

    my_operators = []

    for go in grounded:

        opname = "("+make_name(go.name, go.parameters)+")"

        #god = {"name": opname, "pre": dict(), "eff": dict()}

        god = Operator(opname)

        for i in go.positive_preconditions:
            n = make_name(i[0], i[1:])
            f = Fact(n, True)
            god.pre.add(f)
            fact_names.add(n)
        for i in go.negative_preconditions:
            n = make_name(i[0], i[1:])
            f = Fact(n, False)
            god.pre.add(f)
            fact_names.add(n)
        for i in go.add_effects:
            n = make_name(i[0], i[1:])
            f = Fact(n, True)
            god.eff.add(f)
            fact_names.add(n) 
        for i in go.del_effects:
            n = make_name(i[0], i[1:])
            f = Fact(n, False)
            god.eff.add(f)
            fact_names.add(n)

        my_operators.append(god)

    # Build goal description
    goal = set()
    for f in parser.positive_goals:
        n = make_name(f[0], f[1:])
        goal.add(Fact(n, True))
        fact_names.add(n)
    for f in parser.negative_goals:
        n = make_name(f[0], f[1:])
        goal.add(Fact(n, False))
        fact_names.add(n)

    # Build init state
    init = set()
    for f in fact_names:
        if f in init_facts:
            init.add(Fact(f, True))
        else:
            init.add(Fact(f, False))

    return init, goal, my_operators

