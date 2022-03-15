init = {"cokeServed": False, "cokeInFridge": True}
goal = {"cokeServed": True, "cokeInFridge": True}

#Serve Coke
pre = {"cokeInFridge": True}
eff = {"cokeServed": True, "cokeInFridge": False}
ServeCoke = {"name":"ServeCoke", "pre": pre, "eff": eff}

# RefillFridge
pre = {"cokeInFridge": False}
eff = {"cokeInFridge": True}
RefillFridge = {"name":"RefillFridge", "pre": pre, "eff": eff}

Plan = [ServeCoke, RefillFridge]