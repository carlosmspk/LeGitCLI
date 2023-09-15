from enum import Enum
from dataclasses import dataclass


class ScopeConditionAction(Enum):
    """Defines the action that should be triggered due to a scope condition being met"""

    INCLUDE = "include"
    EXCLUDE = "exclude"


@dataclass(frozen=True)
class ScopeCondition:
    """Pseudo-abstract base data class for all concrete Scope condition dataclasses. A scope condition defines a single condition for a scope to match and how to proceed should the scope match."""

    action: ScopeConditionAction
    """Should the scope match, this dictates the action to be taken. (c.f. ScopeConditionAction enum for possible actions)"""

    def __init_subclass__(cls) -> None:
        if cls.__class__ == ScopeCondition:
            raise TypeError(
                f"Cannot instantiate abstract class {cls.__class__.__name__}."
            )


@dataclass(frozen=True)
class BranchNameScopeCondition(ScopeCondition):
    """Scope Condition that matches the current branch's name with a formatted string

    ### Example
     - Exclude branch named develop:

    ```python
    scope_condition = BranchNameScopeCondition(
        action=ScopeConditionAction.EXCLUDE,
        name_like="develop"
    )
    ```
    """

    name_like: str
    """
    Format string which indicates which branch names to match.

        - TODO: Implement our own class for format strings which have methods to identify and replace certain
    keywords and replace with runtime values (e.g. `'LG[number]-[anything]'` to match a feature branch)
    """
