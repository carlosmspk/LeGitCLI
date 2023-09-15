from dataclasses import dataclass
from typing import Iterable
from model.rules import Rule
from model.scopes import ScopeCondition


@dataclass(frozen=True)
class ScopedRuleSet:
    scope: Iterable[ScopeCondition]
    rules: Iterable[Rule]
