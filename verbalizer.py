import sys
from link_generator import getAllDLinks, getAllELinks
from loadPDDL import loadDomainProblem

if __name__ == "__main__":

    init, goal, operators = loadDomainProblem(sys.argv[1])

    Plan = []
    for a in sys.argv[2:]:
        print(a)
        for o in operators:
            if o["name"] == a:
                Plan.append(o)

    dLinks = getAllDLinks(init, Plan, goal)
    eLinks = [x for x in getAllELinks(init, Plan, goal) if x not in dLinks]

    dLinks = sorted(dLinks, key=lambda x: x[0] )
    eLinks = sorted(eLinks, key=lambda x: x[0] )


    for x in dLinks:
        print(x)
    print("xxx")
    for x in eLinks:
        print(x)
