from enum import Enum
import abstract.guards as guards


class RuleType(Enum):
    """Collection of rule types used to uniquely identify each subclass of Rule. The Enum's value is what should show up in the rule YAML file"""
    COMMIT_MESSAGE_SIZE = "CommitMessageSize"


class Rule:
    """Pseudo-abstract base data class for all concrete rules. A rule is defined by the rule type which gets used to downcast the concrete rule type at runtime."""

    def __init__(self, type: RuleType) -> None:
        guards.prevent_abstract_instantiation(self, Rule)
        self.type = type

    def __repr__(self) -> str:
        """This is to allow all rules to be printable in a human-readable manner for debugging

        Never call this method explicitely, this is Python's way of converting an object to string, which gets automatically
        called, for instance, when calling `print(my_rule)` (Note: this only happens if __str__ is not implemented, which it is not, in this case).
        """
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
        self.max_size = max_size

    @property
    def max_size(self) -> int:
        """Maximum message size (inclusive)"""
        return self.max_size
