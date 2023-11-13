import os
from git.client import GitReadonlyClient


def run_flow(args: list[str]):
    print("Setting up...")

    LEGIT_COMMAND = "legit"
    LEGIT_VALIDATE_COMMAND = f'\n{LEGIT_COMMAND} validate "$1"\n'

    git = GitReadonlyClient()
    dot_git_path = git.get_hooks_path()
    commit_msg_hook_path = os.path.join(dot_git_path, "commit-msg")
    add_legit_command_to_hook(LEGIT_VALIDATE_COMMAND, commit_msg_hook_path)

    print("LeGit setup successfully!")


def add_legit_command_to_hook(LEGIT_VALIDATE_COMMAND, commit_msg_hook_path):
    if not os.path.exists(commit_msg_hook_path):
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
