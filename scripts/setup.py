"""
This script is designed to set up a Python Virtual Environment and
install/update required packages using `poetry`. It checks if a Virtual
Environment exists and, if not, creates one. It also verifies the presence of
Python and Pip binaries and installs the required packages.

The Python version used to run this script will dictate the Virtual
Environment's Python version

Usage:
    Run this script as a standalone application to set up the environment and
    install/update required packages.

"""

if __name__ == "__main__":
    from scriptutils import (
        run_command,
        set_project_root_as_active_dir,
    )
    import sys
    from os.path import join, exists, curdir, abspath

    global_python_command = sys.executable
    project_root_dir = set_project_root_as_active_dir()
    expected_python_cm_dir = join(project_root_dir, ".venv", "bin", "python3")
    expected_pip_cm_dir = join(project_root_dir, ".venv", "bin", "pip")

    run_command(f"{global_python_command} --version")
    run_command(f"poetry --version")

    if not exists("pyproject.toml"):
        print(f"Could not find 'pyproject.toml' file at {abspath(curdir)}")

    venv_changed, pip_called = False, False

    if not exists(join(project_root_dir, ".venv")):
        print("Setting up Python Virtual Environment...")
        run_command(f"{global_python_command} -m venv .venv")
        print("Done!")
        venv_changed = True

    python_command = expected_python_cm_dir if exists(expected_python_cm_dir) else None
    pip_command = expected_pip_cm_dir if exists(expected_pip_cm_dir) else None

    if python_command is None or pip_command is None:
        print(
            "ERROR: Created Virtual environment, but could not find Python and Pip binaries within"
        )
        exit(1)
    run_command(f"poetry env use {expected_python_cm_dir}")
    run_command(f"poetry env info")
    run_command("poetry install --with dev")

    print("All set up!")
