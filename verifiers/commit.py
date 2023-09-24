from typing import Iterable
from git.client import GitReadonlyClient
from model.ruleset import ScopedRuleset
from model.verifier_results import CommitScopedRulesetVerifierResult
from verifiers.ruleset import CommitScopedRulesetVerifier


class CommitVerifier:
    def __init__(self, git_client: GitReadonlyClient) -> None:
        self.__scoped_ruleset_verifier = CommitScopedRulesetVerifier(git_client)

    def verify_commit(
        self, scoped_rulesets: Iterable[ScopedRuleset], commit_message_file: str
    ) -> Iterable[CommitScopedRulesetVerifierResult]:
        triggered_scopes_failing_results = []
        for scoped_ruleset in scoped_rulesets:
            result = self.__scoped_ruleset_verifier.verify_commit_scoped_ruleset(
                scoped_ruleset, commit_message_file
            )
            if result.triggered_scope is not None and result.should_fail:
                triggered_scopes_failing_results.append(result)
        return triggered_scopes_failing_results
