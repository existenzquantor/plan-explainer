import os
import sys
import json
from generation.link_generator import get_all_links
from generation.load_pddl import load_domain_problem

if os.getenv("OPENAI_API_KEY"):
    from verbalization.verbalizer_gpt3  import verbalize
else:
    from verbalization.verbalizer import verbalize

if __name__ == "__main__":

    init, goal, operators = load_domain_problem(sys.argv[1])

    Plan = []
    for a in sys.argv[2].split(";"):
        a = a.lower()
        for o in operators:
            if o["name"] == a:
                Plan.append(o)

    e_links, d_links = get_all_links(init, Plan, goal)
    d_links = sorted(d_links, key=lambda x: (x[3], x[0]) )
    e_links = sorted(e_links, key=lambda x: (x[3], x[0]) )

    # Generate JSON Output
    outputd = dict()
    outputd["D-LINKS"] = d_links
    outputd["E-LINKS"] = e_links
    outputd["VERBALIZATION"] = verbalize(Plan, d_links, e_links)
    print(json.dumps(outputd, indent=2))