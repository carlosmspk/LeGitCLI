"""
This script is designed to create a new subfolder at the project's root directory with the name 'sample_projects', and further creates a subfolder in it named 'default' or a custom name provided by the '--target' argument. It sets up this folder as a Git repository with a single initial commit with a 'content.txt' file.

Usage:
    python create_project.py [--target TARGET_NAME]

Options:
    --target TARGET_NAME    Specify the name of the subfolder to create at the project's root directory. The default name is 'default'.

"""

if __name__ == "__main__":
    import argparse
    import shutil
    import os
    from scriptutils import (
        get_valid_command_from,
        run_command,
        set_project_root_as_active_dir,
    )
    import sys

    project_root_dir = set_project_root_as_active_dir()

    legit_py_dir = os.path.join(project_root_dir, "legit.py")
    if not os.path.exists(legit_py_dir):
        print(
            f"Could not find main.py file to reference. Perhaps either main.py or this script were moved? Expected main.py file to be at: {legit_py_dir}"
        )
        exit(1)

    parser = argparse.ArgumentParser(
        description="Creates a subfolder at folder 'sample_projects' in this project's rootdir. The subfolder itself is named 'default' or whatever name is given by the --target argument, if given. This folder will then be setup to be a git repo with a single commit, and have a content.txt file"
    )
    parser.add_argument("--target", type=str, default="default")
    target: str = os.path.join(
        project_root_dir, "sample_projects", parser.parse_args().target
    )

    python_command = sys.executable

    if get_valid_command_from("git") is None:
        print("Could not find git")
        exit(1)

    if os.path.exists(target):
        invalid_input = True
        while invalid_input:
            user_input = input(
                f"Folder/file '{target}' already exists. Do you wish to remove it? [Y/n]"
            )
            if user_input.lower() in ("y", "yes"):
                shutil.rmtree(target)
                invalid_input = False
            elif user_input.lower() in ("n", "no"):
                print("Aborted.")
                exit(1)
            else:
                print(
                    f"Unrecognized input: '{user_input}'. Please provide one of 'n' or 'y'"
                )

    os.makedirs(target)
    with open(os.path.join(target, "content.txt"), "w") as f:
        f.write("EDIT AND COMMIT ME\n")

    os.chdir(target)
    run_command("git init >/dev/null")
    run_command('git config --local user.name "user" >/dev/null')
    run_command('git config --local user.email "user@mail.com" >/dev/null')
    run_command("git add . >/dev/null")
    run_command('git commit -m "setup" >/dev/null')

    pre_commit_hook_file = os.path.join(".git", "hooks", "pre-commit")

    with open(os.path.join(target, pre_commit_hook_file), "w") as f:
        f.write(f"{python_command} {legit_py_dir}\n")
    os.chmod(pre_commit_hook_file, 0o777)

    print(f"Created new git project at ./{os.path.relpath(target, project_root_dir)}")
