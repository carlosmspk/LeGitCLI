from dataclasses import dataclass
from typing import Iterable
from legitcli.model.rules import Rule
from legitcli.model.scope_conditions import ScopeCondition


@dataclass
class ScopedRuleset:
    """Class with rules to be applied to matching scope conditions, depending on the matched scope action."""

    scope_name: str
    """Human readable name to identify scope"""
    scope: Iterable[ScopeCondition]
    """A combination of scope conditions which defines the scope as a whole. The first scope condition that gets matched defines the outcome of whether rules should be evaluated or not, therefore scope condition order is relevant."""
    ruleset: Iterable[Rule]
    """A combination of rules which defines if the trigger event is valid or should be stopped. Rules are intersected, meaning that all
    rules are "AND"d between each other, and rule order does not matter. """
