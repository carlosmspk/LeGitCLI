from typing import Generic, TypeVar, Union
from legitcli.git.client import GitReadonlyClient
from legitcli.model.scope_conditions import ScopeConditionAction
from legitcli.utils import LazyFileReader
from abc import ABC, abstractmethod

T = TypeVar("T")


class CommitRuleValidatorResult:
    def __init__(self) -> None:
        self.failed = False
        self.fail_reason: Union[str, None] = None

    def set_failed(self, reason: str):
        self.failed = True
        self.fail_reason = reason


class CommitRuleValidator(ABC, Generic[T]):
    def __init__(
        self, rule: T, git: GitReadonlyClient, commit_message_file: LazyFileReader
    ) -> None:
        self._git = git
        self._commit_message_file = commit_message_file
        self._rule = rule

    @abstractmethod
    def validate_commit(self) -> CommitRuleValidatorResult:
        ...


class CommitScopeConditionMatcher(ABC, Generic[T]):
    def __init__(
        self,
        scope_condition: T,
        git: GitReadonlyClient,
        commit_message_file: LazyFileReader,
    ) -> None:
        self._git = git
        self._commit_message_file = commit_message_file
        self._scope_condition = scope_condition

    @abstractmethod
    def get_action(self) -> Union[ScopeConditionAction, None]:
        ...
