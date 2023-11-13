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

To add a scope you can simply add new class that inherits from `ScopeCondition` and annotate it with the YAML `Type` field that you wish that scope condition to match with

#### Example - Create a scope condition for commit author

For a new scope condition which scopes to author, we'd do something like the following in [the scope conditions file](./scopes_conditions.py)

```python
@scope_condition_binds_to_type("AuthorName")
@dataclass
class AuthorNameScopeCondition(ScopeCondition):
    """Scope condition that matches the current user's name"""
    first_name: str
```

This would match the following scope:

```yaml
ScopedRules:
  ...
  - Scope:
    ...
    - Type: AuthorName
      Action: include
      Parameters:
        FirstName: "Bob"
    ...
```

Note that each YAML field's name is automatically inferred from Python's field name (in the previous example: `first_name` (Python) -> `FirstName` (YAML))

## Rules

Rules are the core dataclass for the validators from LeGit's pipeline. A rule defines the conditions for a git event to be valid (i.e., should be allowed to proceed)

### Adding a Rule

The procedure to add a rule is the same as with a scope condition. You can simply add new class that inherits from `Rule` and annotate it with the YAML `Type` field that you wish that scope condition to match with

#### Example - Create a new rule for maximum allowed diffs

For a new rule which limits how many diffs a single commit can have, we could have something like the following in [the rules file](./rules.py)

```python
@rule_binds_to_type("MaxAllowedFileDiff")
@dataclass
class MaxAllowedFileDiffRule(Rule):
    """Rule that prevents commits that change too many lines of code"""
    max_diff_lines: int
```

This would match the following rule:

```yaml
ScopedRules:
  ...
  - Scope:
    ...
    Rules:
    ...
    - Type: MaxAllowedFileDiff
      Parameters:
        MaxDiffLines: 100
    ...
```

Note that each YAML field's name is automatically inferred from Python's field name (in the previous example: `max_diff_lines` (Python) -> `MaxDiffLines` (YAML))

# Scoped Rulesets

Scoped Rulesets simply combine a set of scope conditions (i.e. a Scope) and associate a collection of rules (i.e. a Ruleset). Of particular importance:

- A Scope is deemed to match if all of its scope conditions that are set to `INCLUDE` match, and no scope condition that is set to `EXCLUDE` matches. If no scope conditions match, by default, exclude ruleset.

- The entire pipeline will fail if a single rule mismatches (rules define conditions for a valid git event). All rules from matched scopes should be evaluated, even after first failing rule is found, in order to collect a single result to report which rules failed

- Multiple Scoped Rulesets can be used simultaenously.
