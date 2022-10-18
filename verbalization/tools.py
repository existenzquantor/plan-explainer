def fact_to_string(fact):
    s = list(fact.keys())[0]
    if list(fact.values())[0] == False:
        return "(not " + s + ")"
    else:
        return s