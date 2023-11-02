from typing import Type
from model.exceptions import RedefinedEntityTypeBindingError
from model.scope_conditions import (
    ScopeCondition,
)
from model.bindings import scope_matcher_bindings_map


def matches_scope_condition(scope_condition_type: Type[ScopeCondition]):
    """Binds this ScopeConditionCommitValidator `scope_condition_type` such that this validator will be given the scope condition's parameters and will get called if the scope condition is found on LeGit's rule file."""

    def decorator(cls):
        if scope_condition_type in scope_matcher_bindings_map:
            raise RedefinedEntityTypeBindingError(
                entity="Scope Condition Validator",
                redefined_type=scope_condition_type,
                previously_defined_type=scope_matcher_bindings_map[
                    scope_condition_type
                ],
                attempted_to_define_type=cls,
            )
        scope_matcher_bindings_map[scope_condition_type] = cls
        return cls

    return decorator

