from enum import Enum
import abstract.guards as guards


class RuleType(Enum):
    """Enum which identifies the rule's type. The Enum's value is what should show up in the rule YAML file"""
    COMMIT_MESSAGE_SIZE = "CommitMessageSize"


class Rule:
    """Pseudo-abstract base data class for all concrete rules. A rule is defined by the rule type which gets used to downcast the concrete rule type at runtime."""

    def __init__(self, type: RuleType) -> None:
        guards.prevent_abstract_instantiation(self, Rule)
        self.type = type

    def __repr__(self) -> str:
        """Used to get human-readable output when converted to string (e.g. via `print()`)"""
        return (
            self.__class__.__name__
            + "("
            + ", ".join(
                f"{name}={value}"
                for name, value in self.__dict__.items()
                if not isinstance(value, RuleType)
            )
            + ")"
        )


class CommitMessageSizeRule(Rule):
    """Rule for limiting commit message's size. Maximum size is inclusive."""

    def __init__(self, max_size: int) -> None:
        super().__init__(RuleType.COMMIT_MESSAGE_SIZE)
        self.__max_size = max_size

    @property
    def max_size(self) -> int:
        """Maximum message size (inclusive)"""
        return self.__max_size
