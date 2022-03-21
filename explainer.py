import sys
import json
from link_generator import getAllDLinks, getAllELinks
from load_pddl import loadDomainProblem
import verbalizer

if __name__ == "__main__":

    init, goal, operators = loadDomainProblem(sys.argv[1])

    Plan = []
    for a in sys.argv[2].split(";"):
        for o in operators:
            if o["name"] == a:
                Plan.append(o)

    dLinks = getAllDLinks(init, Plan, goal)
    eLinks = [x for x in getAllELinks(init, Plan, goal) if x not in dLinks]

    dLinks = sorted(dLinks, key=lambda x: (x[3], x[0]) )
    eLinks = sorted(eLinks, key=lambda x: (x[3], x[0]) )


    # Output
    outputd = dict()
    outputd["D-LINKS"] = dLinks
    outputd["E-LINKS"] = eLinks
    outputd["VERBALIZATION"] = verbalizer.verbalize(Plan, dLinks, eLinks)

    print(json.dumps(outputd, indent=2))