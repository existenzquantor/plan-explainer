
def verbalize_enablers(eLinks):
    loc = ""
    for e in eLinks:
        if e[0] == -1:
            loc = loc + e[2].__repr__() + " holds initially and enables " + e[4] + ".\n"
        else:
            if e[-1] == "Goal":
                loc = loc + e[1] + " results in " + e[2].__repr__() + ", which fulfills the goal.\n"
            else:  
                loc = loc + e[1] + " results in " + e[2].__repr__() + ", which enables " + e[4] + ".\n"
    return loc

def verbalize(Plan, dLinks, eLinks):
    """
    It is assumed that the links are already ordered in the order of verbalization.
    """
    glob = dict()
    for i in range(len(Plan)):
        loc = ""
        for d in [x for x in dLinks if x[3] == i]:
            if d[0] == -1:
                loc = loc + d[2].__repr__() + " holds initially and requires " + d[4] + ".\n"
            else:
                loc = loc + d[1] + " results in " + d[2].__repr__() + ", which requires " + d[4] + ".\n"
        loc = loc + verbalize_enablers([x for x in eLinks if (x[0] == i or (x[0] == -1 and x[3] == i))])
        glob["ACTION"+str(i)] = loc
    return glob

    
    
    
    
    
    


