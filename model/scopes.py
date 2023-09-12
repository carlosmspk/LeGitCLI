from enum import Enum
from dataclasses import dataclass


class ScopeAction(Enum):
    INCLUDE = "include"
    EXCLUDE = "exclude"


@dataclass
class Scope:
    action: ScopeAction

    def __init_subclass__(cls) -> None:
        if cls.__class__ == Scope:
            raise TypeError(
                f"Cannot instantiate abstract class {cls.__class__.__name__}."
            )
