from dataclasses import dataclass, field
from typing import Set

@dataclass(frozen = True, eq = True)
class Fact:
    name: str
    value: bool

    def __repr__(self) -> str:
        if not self.value:
            return "(not ("+self.name+"))"
        else:
            return "("+self.name+")"

@dataclass(frozen = True, eq = True)
class Operator:
    name: str
    pre: Set[Fact] = field(default_factory=set) 
    eff: Set[Fact] = field(default_factory=set)

