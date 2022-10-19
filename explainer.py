import os
import sys
import json
from generation.link_generator import generate_explanations
from generation.load_pddl import load_domain_problem, make_plan
from verbalization.verbalizer import verbalize

if __name__ == "__main__":

    # Generate explanations
    init, goal, operators = load_domain_problem(sys.argv[1])
    plan = make_plan(operators)
    e_links, d_links = generate_explanations(init, plan, goal)

    # Verbalize explanations
    verbalization = verbalize(plan, d_links, e_links)

    # Generate JSON Output
    outputd = dict()
    outputd["D-LINKS"] = d_links
    outputd["E-LINKS"] = e_links
    outputd["VERBALIZATION"] = verbalization
    print(json.dumps(outputd, indent=2))