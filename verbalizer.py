
def fact_to_string(fact):
    s = list(fact.keys())[0]
    if list(fact.values())[0] == False:
        return "(not " + s + ")"
    else:
        return s

def verbalize_enablers(eLinks):
    loc = ""
    for e in eLinks:
        if e[0] == -1:
            loc = loc + fact_to_string(e[2]) + " holds initially and enables " + e[4] + ".\n"
        else:
            if e[-1] == "Goal":
                loc = loc + e[1] + " results in " + fact_to_string(e[2]) + ", which fulfills the goal.\n"
            else:  
                loc = loc + e[1] + " results in " + fact_to_string(e[2]) + ", which enables " + e[4] + ".\n"
    return loc

def verbalize(Plan, dLinks, eLinks):
    """
    It is assumed that the links are already ordered in the order of verbalization.
    """
    glob = dict()
    for i in range(len(Plan)):
        loc = ""
        #loc = loc + "\nACTION "+ str(i) + "\n"
        for d in [x for x in dLinks if x[3] == i]:
            if d[0] == -1:
                loc = loc + fact_to_string(d[2]) + " holds initially and requires " + d[4] + ".\n"
            else:
                loc = loc + d[1] + " results in " + fact_to_string(d[2]) + ", which requires " + d[4] + ".\n"
        loc = loc + verbalize_enablers([x for x in eLinks if (x[0] == i or (x[0] == -1 and x[3] == i))])
        glob["ACTION"+str(i)] = loc
    return glob

    
    
    
    
    
    


