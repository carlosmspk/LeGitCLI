import subprocess


def run_command(command: str, abort_on_fail: bool = True) -> str:
    """
    Executes a command and returns its result, including stdout and exit code.
    """
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, text=True, check=abort_on_fail
    )
    return result.stdout
