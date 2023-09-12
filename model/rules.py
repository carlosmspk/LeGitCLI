from enum import Enum


class RuleType(Enum):
    COMMIT_MESSAGE_SIZE = "CommitMessageSize"


class Rule:
    def __init__(self, type: RuleType) -> None:
        if self.__class__ == Rule:
            raise TypeError(
                f"Cannot instantiate abstract class {self.__class__.__name__}."
            )
        self.type = type

    def __repr__(self) -> str:
        return (
            self.__class__.__name__
            + "("
            + ", ".join(f"{name}={value}" for name, value in self.__dict__.items())
            + ")"
        )


class CommitMessageSizeRule(Rule):
    def __init__(self, max_size: int) -> None:
        super().__init__(RuleType.COMMIT_MESSAGE_SIZE)
        self.max_size = max_size

    def __str__(self) -> str:
        return super().__str__()
