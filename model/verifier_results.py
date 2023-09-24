from dataclasses import dataclass
from model.rules import Rule


@dataclass(frozen=True)
class FailedRule:
    rule: Rule
    container_scope_name: str
    failed_reason: str


@dataclass(frozen=True)
class CommitScopedRulesetVerifierResult:
    triggered_scope: str | None
    should_fail: bool
    failed_rules: list[FailedRule] = tuple()
