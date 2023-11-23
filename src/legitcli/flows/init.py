from os.path import join, exists, relpath
from os import pardir, curdir
from typing import List
from legitcli.git.client import GitReadonlyClient

MINIMAL_LEGIT_RULES_FILE = r"""
# For generic configurations that do not pertain to rules or scopes, but rather
# on how LeGit analyzes and applies this file
Config: {}
# Rules that should be applied to all cases, regardless of scope
GenericRules: []
# Rules with specific scopes attached to them
ScopedRules: []
"""


def run_flow(args: List[str]):
    print("Setting up...")

    LEGIT_COMMAND = "legit"
    LEGIT_VALIDATE_COMMAND = f'\n{LEGIT_COMMAND} validate "$1"\n'

    git = GitReadonlyClient()
    dot_git_path = git.get_hooks_path()
    commit_msg_hook_path = join(dot_git_path, "commit-msg")
    add_legit_command_to_hook(LEGIT_VALIDATE_COMMAND, commit_msg_hook_path)
    add_legit_rules_file(relpath(curdir, join(git.get_dot_git_path(), pardir)))

    print("LeGit setup successfully!")


def add_legit_command_to_hook(LEGIT_VALIDATE_COMMAND, commit_msg_hook_path):
    if not exists(commit_msg_hook_path):
        with open(commit_msg_hook_path, "w") as hookfile:
            print(f"Created commit hook at {commit_msg_hook_path}")
            hookfile.write(LEGIT_VALIDATE_COMMAND)
    else:
        with open(commit_msg_hook_path, "r") as hookfile:
            print(f"Found commit hook at {commit_msg_hook_path}")
            configured = False
            for line in hookfile.readlines():
                if LEGIT_VALIDATE_COMMAND in line:
                    print("Hook was already configured, skipping...")
                    configured = True
                    break
        if not configured:
            with open(commit_msg_hook_path, "a") as hookfile:
                hookfile.write(LEGIT_VALIDATE_COMMAND)


def add_legit_rules_file(project_path: str):
    expected_legit_rules_path = join(project_path, "legitrules.yml")
    if exists(expected_legit_rules_path):
        print(f"LeGit rules file was found at {expected_legit_rules_path}")
    else:
        with open(expected_legit_rules_path, "w") as rulesfile:
            rulesfile.write(MINIMAL_LEGIT_RULES_FILE)
        print(f"LeGit rules file created at {expected_legit_rules_path}")
