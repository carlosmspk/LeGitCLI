from dataclasses import dataclass
from typing import Sequence, Union
from legitcli.model.rules import Rule


@dataclass
class FailedRule:
    rule: Rule
    failed_reason: str


@dataclass
class CommitScopedRulesetValidatorResult:
    triggered_scope: Union[str, None]
    should_fail: bool
    failed_rules: Sequence[FailedRule] = tuple()
