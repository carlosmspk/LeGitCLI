from argparse import ArgumentParser
from typing import List
from legitcli.git.client import GitReadonlyClient
from legitcli.parsing import parse_legit_file
from legitcli.utils import LazyFileReader
from legitcli.validator.commit import CommitValidator
from legitcli.model.globals import Globals


class FlowArgs:
    def __init__(self, args: List[str]) -> None:
        parser = ArgumentParser(
            prog="legit validate",
            description="validate ongoing commit, given commit message file",
        )
        parser.add_argument("message-file", help="path of file with commit message")
        parser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="if true, prints extra info as to which scopes are checked and their results",
        )
        parser.add_argument(
            "-r",
            "--rules-file",
            help="path of file with legit rules. By default, uses 'legitrules.yml' in current directory",
            default="legitrules.yml",
        )
        prased_args = {
            key: value for (key, value) in parser.parse_args(args)._get_kwargs()
        }
        self.rules_path: str = prased_args["rules_file"]
        self.verbose: bool = prased_args["verbose"]
        self.commit_message_path: str = prased_args["message-file"]


def run_flow(args: List[str]):
    """This flow validates an ongoing git process, such as a commit, and exits
    with exit code 0 if git process is valid, or non-zero otherwise"""
    flow_args = FlowArgs(args)
    if flow_args.verbose:
        Globals.verbose = True

    legit_file = LazyFileReader(flow_args.rules_path)

    commit_message_file = LazyFileReader(flow_args.commit_message_path)

    scoped_rulesets, config = parse_legit_file(legit_file)

    validator = CommitValidator(GitReadonlyClient(), commit_message_file, config)
    triggered_scopes_results = validator.validate_commit(scoped_rulesets)
    failed_triggered_scopes_results = list(
        filter(lambda x: x.should_fail, triggered_scopes_results)
    )

    if Globals.verbose:
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
