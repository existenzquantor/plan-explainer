init = {"inOffice": True, "inLab": False, "doorOpen": False, "officeSoundProtected": True}
goal = {"inLab": True, "officeSoundProtected": True}

#askHumanOpenDoor
pre = {}
eff = {"doorOpen": True, "officeSoundProtected": False}
askHumanOpenDoor = {"name":"askHumanOpenDoor", "pre": pre, "eff": eff}

# askHumanCloseDoor
pre = {}
eff = {"doorOpen": False, "officeSoundProtected": True}
askHumanCloseDoor = {"name":"askHumanCloseDoor", "pre": pre, "eff": eff}


# moveOfficeLab
pre = {"inOffice": True, "doorOpen": True}
eff = {"inOffice": False, "inLab": True}
moveOfficeLab = {"name":"moveOfficeLab", "pre": pre, "eff": eff}

Plan = [askHumanOpenDoor, moveOfficeLab, askHumanCloseDoor]