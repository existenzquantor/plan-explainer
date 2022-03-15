import sys
from link_generator import getAllDLinks, getAllELinks

if __name__ == "__main__":
    my = __import__(sys.argv[1])

    dLinks = getAllDLinks(my.init, my.Plan, my.goal)
    eLinks = [x for x in getAllELinks(my.init, my.Plan, my.goal) if x not in dLinks]

    dLinks = sorted(dLinks)
    eLink = sorted(eLinks)

    for i in range(-1, len(my.Plan)):
        pass