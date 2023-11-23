from enum import Enum
from dataclasses import dataclass
from legitcli.model.annotations import scope_condition_binds_to_type
from legitcli.typeutils import guards


class ScopeConditionAction(Enum):
    """Defines the action that should be triggered due to a scope condition being met"""

    INCLUDE = "include"
    EXCLUDE = "exclude"


@dataclass
class ScopeCondition:
    """Pseudo-abstract base data class for all concrete Scope condition dataclasses. A scope condition defines a single condition for a scope to match and how to proceed should the scope match."""

    action: ScopeConditionAction
    """Should the scope match, this dictates the action to be taken. (c.f. ScopeConditionAction enum for possible actions)"""

    def __post_init__(self) -> None:
        guards.prevent_abstract_instantiation(self, ScopeCondition)


@scope_condition_binds_to_type("BranchName")
@dataclass
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


@dataclass
class AlwaysTrueScopeCondition(ScopeCondition):
    """Scope Condition that always matches as true. Used for generic rules that should always apply"""
