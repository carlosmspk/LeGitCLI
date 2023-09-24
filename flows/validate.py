import os
from git.client import GitReadonlyClient
from parsing import parse_legit_file
from verifiers.commit import CommitVerifier

__LEGIT_FILE_PATH = "legitrules.yml"
__DEV_MODE=True #TODO: define this as command arg


def run_flow():
    """This flow validates an ongoing git process, such as a commit, and exits
    with exit code 0 if git process is valid, or non-zero otherwise"""
    if not __DEV_MODE and __LEGIT_FILE_PATH not in os.listdir(os.curdir):
        raise FileNotFoundError("Could not find required file 'legitrules.yml'")

    dummy_commit_message_file = (
        "dummy.txt"  # TODO: retrieve this as argument to legit CLI
    )

    scoped_rulesets, config = parse_legit_file(__LEGIT_FILE_PATH)

    verifier = CommitVerifier(GitReadonlyClient())
    triggered_scopes_failing_results = verifier.verify_commit(scoped_rulesets, dummy_commit_message_file)

    if __DEV_MODE:
        for failing_scope_result in triggered_scopes_failing_results:
            failed_rules_message ="\n\t- " + "\n\t- ".join(i.failed_reason for i in failing_scope_result.failed_rules)
            print(f"Scope '{failing_scope_result.triggered_scope}' was triggered and failed because:{failed_rules_message}")

    # TODO: display better info as to why commit failed
    if len(triggered_scopes_failing_results) > 0:
        exit(1)


def validate_commit():
    ...
