from command import run_command
import os


class GitReadonlyClient:
    """
    Client class that acts upon a git repository found in the process's current
    directory, but does not change the repository's state
    """

    def get_current_branch(self) -> str:
        return run_command("git rev-parse --abbrev-ref HEAD").strip()

    def get_author(self) -> tuple[str, str]:
        """
        Returns the configured user/author. Result is returned as tuple of name
        and email, respectively
        """
        return (
            run_command("git config user.name").strip(),
            run_command("git config user.email").strip(),
        )


class GitClient(GitReadonlyClient):
    """
    Client class that acts upon a git repository found in the process's current
    directory.
    """

    def init(self, main_branch: str | None):
        """Initializes a git repository at current directory. Accepts an initial
        main branch name (default: 'main').

        Raises an exception if init fails, e.g. because directory is already
        initialized as a git repo."""
        git_dir = os.path.abspath(".git")
        if os.path.exists(git_dir):
            raise FileExistsError(
                f"Can't initialize git repo because .git folder already exists at {git_dir}"
            )
        command = "git init"
        if main_branch:
            command += f" -b {main_branch}"
        run_command(command)

    def commit(self, message: str):
        """
        Commits staged changes with `message`.

        Raises an exception if commit fails, e.g. because there are no staged
        files or message is invalid.
        """
        run_command(f'git commit -m "{message}"')

    def stage(self, file_path: str | None):
        """
        Stages `file_path` for committing.

        Raises an exception if stage fails, e.g. because file does not exist or
        has no changes.
        """
        command = "git add "
        if file_path is None:
            command += "."
        else:
            command += file_path
        run_command(command)

    add = stage
