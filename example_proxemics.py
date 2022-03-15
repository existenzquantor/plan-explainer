init = {"atGoalPose": False, "violation": False}
goal = {"atGoalPose": True, "violation": False}

#Pass Close By
pre = {}
eff = {"atGoalPose": True, "violation": True}
PassCloseBy = {"name":"PassCloseBy", "pre": pre, "eff": eff}

# RefillFridge
pre = {}
eff = {"violation": False}
SaySorry = {"name":"SaySorry", "pre": pre, "eff": eff}

Plan = [PassCloseBy, SaySorry]