from model.config import Config
from model.ruleset import ScopedRuleset
import model.scope_conditions as scope_conditions
import model.rules as rules


def parse_legit_file(legit_file_path: str) -> tuple[list[ScopedRuleset], Config]:
    # TODO: Replace with actual implementation
    return [
        ScopedRuleset(
            scope_name="Commits to Develop Branch",
            scope=scope_conditions.BranchNameScopeCondition(
                action=scope_conditions.ScopeConditionAction.INCLUDE,name_like="develop"
            ),
            ruleset=[rules.CommitMessageSizeRule(100)],
        )
    ], Config()
