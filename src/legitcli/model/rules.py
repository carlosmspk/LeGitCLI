from dataclasses import dataclass
from legitcli.model.annotations import rule_binds_to_type
from legitcli.typeutils import guards


class Rule:
    """Pseudo-abstract base data class for all concrete rules. A rule is defined by the rule type which gets used to downcast the concrete rule type at runtime."""

    def __init__(self) -> None:
        guards.prevent_abstract_instantiation(self, Rule)


@rule_binds_to_type("CommitMessageSize")
@dataclass
class CommitMessageSizeRule(Rule):
    """Rule for limiting commit message's size. Maximum size is inclusive."""

    max_size: int
    """Maximum message size (inclusive)"""


@rule_binds_to_type("CommitMessageText")
@dataclass
class CommitMessageTextRule(Rule):
    """Rule for asserting that Commit Message complies with given regex."""

    message_regex: str
    """Regex used for matching commit message. If regex matches, commit is allowed to proceed"""

    ignore_newlines: bool = False
    """Whether to consider newlines in the regex or not. If False, message is evaluated as a whole and regex should account for newlines. If True, any consecutive newlines will be replaced with a single space"""
