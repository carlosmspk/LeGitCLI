import subprocess


def run_command(command: str) -> str:
    """
    Executes a command and returns its result, including stdout and exit code.
    """
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, text=True, check=True
    )
    return result.stdout
