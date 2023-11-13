from typing import List
from legitcli.git.client import GitReadonlyClient
from legitcli.model.config import Config
from legitcli.model.ruleset import ScopedRuleset
from legitcli.model.validator_results import CommitScopedRulesetValidatorResult
from legitcli.utils import LazyFileReader
from legitcli.validator.ruleset import CommitScopedRulesetValidator


class CommitValidator:
    def __init__(
        self,
        git_client: GitReadonlyClient,
        commit_message_file: LazyFileReader,
        config: Config,
    ) -> None:
        self.__scoped_ruleset_validator = CommitScopedRulesetValidator(
            git_client, commit_message_file, config
        )

    def validate_commit(
        self, scoped_rulesets: List[ScopedRuleset]
    ) -> List[CommitScopedRulesetValidatorResult]:
        triggered_scopes_results = []
        for scoped_ruleset in scoped_rulesets:
            result = self.__scoped_ruleset_validator.validate_commit_scoped_ruleset(
                scoped_ruleset
            )
            if result.triggered_scope is not None:
                triggered_scopes_results.append(result)
        return triggered_scopes_results
