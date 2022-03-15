import sys
from link_generator import getAllDLinks, getAllELinks

if __name__ == "__main__":
    print(sys.argv[1])
    my = __import__(sys.argv[1])

    print("D-LINKS")
    dLinks = getAllDLinks(my.init, my.Plan, my.goal)
    for d in dLinks:
        print(d)


    print("E-LINKS")
    eLinks = [x for x in getAllELinks(my.init, my.Plan, my.goal) if x not in dLinks]
    for e in eLinks:
        print(e)