def fact_to_string(fact):
    s, t = list(fact.items())[0]
    if not t:
        return "(not " + s + ")"
    else:
        return s