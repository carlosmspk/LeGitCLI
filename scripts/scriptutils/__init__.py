from __future__ import annotations
import os


def run_command(command: str, abort_on_error: bool = True) -> int:
    """
    Executes a command and returns the exit code, with an option to abort the
    script if the command fails.

    ### Args
     - `command`: string that represents the command you want to run. It can be
       any valid command that can be executed in the command line
     - `abort_on_error`: boolean flag that determines whether the script should
       abort if the command fails. If `abort_on_error` is set to `True`, the
       script will print an error message and exit with a status code of 1 if
       the previous command returns a non-zero, defaults to `True`

    ### Returns Integer value, which is the exit code of the command that was
    executed.
    """
    exit_code = os.system(command)
    if exit_code != 0 and abort_on_error:
        print(
            f"\nERROR: Aborting script because previous command failed.\nFailed command:\n\t{command}"
        )
        exit(1)
    return exit_code


def get_valid_command_from(commands: str | tuple[str]) -> str | None:
    """
    Checks if a command is valid and returns the first valid command from a
    given list of commands.
    
    ### Args - `commands` parameter can be either a string or a tuple of
    strings. It represents a list of commands that you want to check for
    validity, or just the single command

    ### Returns String representing a valid command which was found, or `None`
    if no valid command is found.
    """
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
    """
    Sets the project root directory as the active directory and returns the path of the
    project root directory.
    
    ### Returns
    String with project root directory.
    """
    project_root_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    )
    os.chdir(project_root_dir)
    return project_root_dir
