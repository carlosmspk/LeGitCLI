from typing import Type
from model.rules import Rule
from model.exceptions import RedefinedEntityTypeBindingError
from model.bindings import rule_validator_bindings_map


def validates_rule(rule_type: Type[Rule]):
    """Binds this RuleCommitValidator `rule_type` such that this validator will be given the rule's parameters and will get called if the rule is found on LeGit's rule file."""

    def decorator(cls):
        if rule_type in rule_validator_bindings_map:
            raise RedefinedEntityTypeBindingError(
                entity="Rule Validator",
                redefined_type=rule_type,
                previously_defined_type=rule_validator_bindings_map[rule_type],
                attempted_to_define_type=cls,
            )
        rule_validator_bindings_map[rule_type] = cls
        return cls

    return decorator
