
def verbalize_enablers(eLinks):
    loc = ""
    for e in eLinks:
        if e[0] == -1:
            loc = loc + str(e[2]) + " holds initially and enables " + e[4] + ". "
        else:
            loc = loc + e[1] + " results in " + str(e[2]) + ", which enables " + e[4] + ". "
    return loc

def verbalize(dLinks, eLinks):
    """
    It is assumed that the links are already ordered in the order of verbalization.
    """
    glob = ""
    loc = ""
    step = -1
    for d in dLinks:
        if step != d[3]:
            if step != -1:
                loc = loc + verbalize_enablers([x for x in eLinks if x[0] == step])
            step = d[3]
            glob = glob + loc
            loc = ""
        if d[0] == -1:
            loc = loc + str(d[2]) + " holds initially and requires " + d[4] + ". "
        else:
            loc = loc + d[1] + " results in " + str(d[2]) + ", which requires " + d[4] + ". "

    return glob + loc + verbalize_enablers([x for x in eLinks if x[0] == step])
