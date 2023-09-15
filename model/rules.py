from enum import Enum
import abstract.guards as guards


class RuleType(Enum):
    COMMIT_MESSAGE_SIZE = "CommitMessageSize"


class Rule:
    def __init__(self, type: RuleType) -> None:
        guards.prevent_abstract_instantiation(self, Rule)
        self.type = type

    def __repr__(self) -> str:
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
    def __init__(self, max_size: int) -> None:
        super().__init__(RuleType.COMMIT_MESSAGE_SIZE)
        self.max_size = max_size

    @property
    def max_size(self) -> int:
        return self.max_size
