
init = {"hasKey": False, "open": False, "locked": True, "inA": True, "inB": False}
goal = {"inB":True, "locked": True}

# Fetch Key
pre = {"hasKey": False}
eff = {"hasKey": True}
FetchKey = {"name":"FetchKey", "pre": pre, "eff": eff}

# Open Door
pre = {"open": False, "locked": False}
eff = {"open": True}
OpenDoor = {"name":"OpenDoor", "pre": pre, "eff": eff}

# Unlock Door
pre = {"locked": True, "open": False, "hasKey": True}
eff = {"locked": False}
UnlockDoor = {"name":"UnlockDoor","pre": pre, "eff": eff}

# Lock Door
pre = {"locked": False, "open": False, "hasKey": True}
eff = {"locked": True}
LockDoor = {"name":"LockDoor","pre": pre, "eff": eff}

# Close Door
pre = {"open": True}
eff = {"open": False}
CloseDoor = {"name":"CloseDoor", "pre": pre, "eff": eff}

# moveAtoB
pre = {"inA": True, "inB": False, "open": True}
eff = {"inA": False, "inB": True}
moveAtoB = {"name":"MoveAtoB", "pre": pre, "eff": eff}

Plan = [FetchKey, UnlockDoor, OpenDoor, moveAtoB, CloseDoor, LockDoor]