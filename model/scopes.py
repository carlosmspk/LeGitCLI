from enum import Enum
from dataclasses import dataclass


class ScopeConditionAction(Enum):
    INCLUDE = "include"
    EXCLUDE = "exclude"


@dataclass(frozen=True)
class ScopeCondition:
    action: ScopeConditionAction

    def __init_subclass__(cls) -> None:
        if cls.__class__ == ScopeCondition:
            raise TypeError(
                f"Cannot instantiate abstract class {cls.__class__.__name__}."
            )


@dataclass(frozen=True)
class BranchNameScopeCondition(ScopeCondition):
    name_like: str
