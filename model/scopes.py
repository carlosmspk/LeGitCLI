from enum import Enum
from dataclasses import dataclass


class ScopeAction(Enum):
    INCLUDE = "include"
    EXCLUDE = "exclude"


@dataclass(frozen=True)
class Scope:
    action: ScopeAction

    def __init_subclass__(cls) -> None:
        if cls.__class__ == Scope:
            raise TypeError(
                f"Cannot instantiate abstract class {cls.__class__.__name__}."
            )


@dataclass(frozen=True)
class BranchNameScope(Scope):
    name_like: str
