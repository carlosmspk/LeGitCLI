from __future__ import annotations
import os
from os import pardir as previous_dir


def run_command(command: str, abort_on_error: bool = True) -> int:
    exit_code = os.system(command)
    if exit_code != 0 and abort_on_error:
        print(
            f"\nERROR: Aborting script because previous command failed.\nFailed command:\n\t{command}"
        )
        exit(1)
    return exit_code


def get_valid_command_from(commands: str | tuple[str]) -> str | None:
    if isinstance(commands, str):
        command = commands
        if run_command(f"which {command} >/dev/null", abort_on_error=False):
            return None
        else:
            return command
    else:
        try:
            return next(
                filter(
                    lambda command: get_valid_command_from(command) is not None,
                    commands,
                )
            )
        except:
            return None


def set_project_root_as_active_dir() -> str:
    project_root_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), previous_dir, previous_dir)
    )
    os.chdir(project_root_dir)
    return project_root_dir
