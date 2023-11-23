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
