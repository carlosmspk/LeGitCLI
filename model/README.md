# Model

Model classes that behave as data classes, having little to no behavior. Avoid, as much as possible, implementing methods for these classes

Noteworthy Model types:

 - [Config](#config)
 - [Scopes](#scopes)
 - [Rules](#rules)
 - [ScopedRuleSet](#scoped-rule-sets)

## Config

`(TODO)` Config defines higher level definitions of how LeGit should behave.

## Scopes

Scopes define when the corresponding rules should be applied. A scope can include its matching conditions so that matches lead to the rules being applied, or they can be exclusive, such that a matching scope imediately discards any rule validation. A scope, by itself, can never invalidate a git event

This can be useful in the scenario that we may want to create exceptions. E.g.:
 - scope condition 1: "I want all local commits by author 'admin@mail.com' to be allowed (exclusive)"
 - scope condition 2: "I want to check all commits to develop (inclusive)"

Depending on the scope condition order this could translate to "only evaluate non-admin commits to develop" or to "only evaluate admin commits on develop"

### Adding a Scope Condition

To add a scope you can simply add new class that inherits from Scope

#### Example - Create a scope condition for commit author

For a new scope condition which scopes to author, we'd do something like the following in [the scope conditions file](./scopes_conditions.py)

```python
@dataclass(frozen=True)
class AuthorNameScopeCondition(ScopeCondition):
    """Scope condition that matches the current user's name"""
    author_name: str
```

## Rules

Rules are the core dataclass for the validators from LeGit's pipeline. A rule defines the conditions for a git event to be valid (i.e., should be allowed to proceed)

### Adding a Rule

To add a rule you can follow the steps:
 1 - Add the rule's name as should be stated in LeGit's rule file as a rule type
 2 - Create a new subclass of Rule, which initializes the abstract Rule with the given rule type above

#### Example - Create a new rule for maximum allowed diffs

For a new rule which limits how many diffs a single commit can have, we could have something like the following in [the rules file](./rules.py)

```python
class RuleType(Enum):
    ...
    MAX_ALLOWED_FILE_DIFF = "MaxAllowedFileDiff"

...

class MaxAllowedFileDiffRule(Rule):
    """Limits how much diff per file is allowed for a single commit."""

    def __init__(self, max_diff_lines: int) -> None:
        super().__init__(RuleType.MAX_ALLOWED_FILE_DIFF)
        self.max_diff_lines = max_diff_lines

    @property
    def max_diff_lines(self) -> int:
        """Maximum line diff per file (inclusive)"""
        return self.max_diff_lines
```

# Scoped Rulesets

Scoped Rulesets simply combine a set of scope conditions (i.e. a Scope) and associate a collection of rules (i.e. a Ruleset). Of particular importance:
 - Scope conditions should be evaluated on first-match (order is relevant): check each scope condition, if it matches, use that scope condition's action immediately; if it does not match, carry on to check if the next scope condition matches, and so on... If no scope conditions match, by default, exclude ruleset

 - All rules should be evaluated. The entire pipeline will fail if a single rule mismatches (rules define conditions for a valid git event). However, all rules should be validated, in order to collect a single result to report which rules failed