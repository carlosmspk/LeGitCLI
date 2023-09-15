from dataclasses import dataclass
from model.rules import Rule
from model.scopes import ScopeCondition


@dataclass(frozen=True)
class ScopedRuleSet:
    scope: list[ScopeCondition]
    rules: list[Rule]
