"""
This script is designed to set up a Python Virtual Environment and
install/update required packages listed in 'requirements.txt' within the project
directory. It checks if a Virtual Environment exists and, if not, creates one.
It also verifies the presence of Python and Pip binaries and installs the
required packages. After execution, it provides instructions on how to activate
and deactivate the Virtual Environment manually.

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
    from os.path import join, exists

    def run() -> tuple[str, str]:
        project_root_dir = set_project_root_as_active_dir()
        pip_requirements_txt = join(project_root_dir, "requirements.txt")
        expected_python_cm_dir = join(project_root_dir, ".venv", "bin", "python3")
        expected_pip_cm_dir = join(project_root_dir, ".venv", "bin", "pip")

        venv_changed, pip_called = False, False

        if not exists(join(project_root_dir, ".venv")):
            global_python_command = sys.executable
            print("Setting up Python Virtual Environment...")
            run_command(f"{global_python_command} -m venv .venv")
            print("Done!")
            venv_changed = True

        python_command = (
            expected_python_cm_dir if exists(expected_python_cm_dir) else None
        )
        pip_command = expected_pip_cm_dir if exists(expected_pip_cm_dir) else None

        if python_command is None or pip_command is None:
            print(
                "ERROR: Created Virtual environment, but could not find Python and Pip binaries within"
            )
            return (venv_changed, pip_called)

        if not exists(pip_requirements_txt):
            print(
                "Required packages file 'requirements.txt' could not be found. Skipping updates..."
            )
        else:
            print("Installing/Updating missing Python modules from 'requirements.txt'")
            run_command(f"{python_command} -m pip install --upgrade pip >/dev/null")
            run_command(f"{pip_command} install -r requirements.txt -q")
            pip_called = True
            print("Done!")

        return (venv_changed, pip_called)

    venv_changed, pip_changed = run()

    if not pip_changed and not pip_changed:
        print("Nothing to do.")
    elif venv_changed:
        print(
            "\nVirtual Environment was created. Most IDEs should detect it and ask you if you want to activate it for this project, but you can set it as active manually by running command:\n\tsource .venv/bin/activate\n\nYou'll know this worked if your terminal's input is now preppended with (.venv). Although rarely necessary you can deactivate the virtual environment by running command:\n\tdeactivate\n\nVirtual environments are always deactivated on new terminals, you'll have to activate it everytime if you want to run Python manually via terminal."
        )
