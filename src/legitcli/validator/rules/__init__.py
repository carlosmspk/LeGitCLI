from typing import Type
from legitcli.model.rules import CommitMessageSizeRule, Rule
from legitcli.validator.generic import CommitRuleValidator, CommitRuleValidatorResult
from legitcli.model.exceptions import RedefinedEntityTypeBindingError
from legitcli.model.bindings import rule_validator_bindings_map


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


@validates_rule(CommitMessageSizeRule)
class CommitMessageSizeValidator(CommitRuleValidator[CommitMessageSizeRule]):
    def validate_commit(self) -> CommitRuleValidatorResult:
        result = CommitRuleValidatorResult()
        commit_message = self._commit_message_file.read()
        commit_message_size = 0
        for line in commit_message:
            comment_token_index = line.strip().find("#")
            if comment_token_index != 0:
                commit_message_size += len(line)

        if commit_message_size > self._rule.max_size:
            result.set_failed(
                f"Expected a maximum commit message size of {self._rule.max_size}, but commit message is {commit_message_size} characters long"
            )

        return result
