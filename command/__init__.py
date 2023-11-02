import subprocess


def run_command(command: str, abort_on_error: bool = True) -> str:
    """
    Executes a command and returns its result, including stdout and exit code.
    """
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, text=True, check=abort_on_error
    )
    return result.stdout


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
        if (
            run_command(f"which {command} >/dev/null", abort_on_error=False).returncode
            != 0
        ):
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
