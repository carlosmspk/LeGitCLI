from git.client import GitReadonlyClient
from parsing import parse_legit_file
from utils import LazyFileReader
from validator.commit import CommitValidator

__DEV_MODE = True  # TODO: define this as command arg


def run_flow():
    """This flow validates an ongoing git process, such as a commit, and exits
    with exit code 0 if git process is valid, or non-zero otherwise"""
    legit_file = LazyFileReader(
        "legitrules.yml" if not __DEV_MODE else "resources/rulefiles/samples/simple.yml"
    )

    commit_message_file = LazyFileReader(
        "resources/message/short_message.txt"
    )  # TODO: retrieve this as argument to legit CLI

    scoped_rulesets, config = parse_legit_file(legit_file)

    validator = CommitValidator(GitReadonlyClient(), commit_message_file, config)
    triggered_scopes_results = validator.validate_commit(scoped_rulesets)
    failed_triggered_scopes_results = list(
        filter(lambda x: x.should_fail, triggered_scopes_results)
    )

    if __DEV_MODE:
        for failing_scope_result in triggered_scopes_results:
            failed_rules_message = (
                "and failed because:\n\t- "
                + "\n\t- ".join(
                    i.failed_reason for i in failing_scope_result.failed_rules
                )
                if failing_scope_result.should_fail
                else "and was validated."
            )
            print(
                f"Scope '{failing_scope_result.triggered_scope}' was triggered {failed_rules_message}"
            )
        if len(triggered_scopes_results) < 1:
            print(f"No scopes were triggered. Nothing to do.")

    # TODO: display better info as to why commit failed
    if len(failed_triggered_scopes_results) > 0:
        exit(1)


def validate_commit():
    ...
