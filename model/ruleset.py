from dataclasses import dataclass
from model.rules import Rule
from model.scopes import Scope


@dataclass(frozen=True)
class ScopedRuleSet:
    scope: Scope
    rules: list[Rule]
