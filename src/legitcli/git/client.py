from typing import Union, Tuple
from legitcli.command import run_command
import os


class GitReadonlyClient:
    """
    Client class that acts upon a git repository found in the process's current
    directory, but does not change the repository's state
    """

    def get_current_branch(self) -> str:
        return run_command("git rev-parse --abbrev-ref HEAD").strip()

    def get_author(self) -> Tuple[Union[str, None], Union[str, None]]:
        """
        Returns the configured user/author. Result is returned as tuple of name
        and email, respectively
        """
        return (
            self.get_config("user.name"),
            self.get_config("user.email"),
        )

    def get_dot_git_path(self) -> str:
        """
        Returns the relative path to the `.git` directory.
        """

        return run_command("git rev-parse --git-dir").strip()

    def get_config(self, config_key: str) -> Union[str, None]:
        """
        Retrieves a Git configuration value based on the provided configuration
        key, or `None`, if the given `config_key` does not exist.
        """
        return run_command(f"git config {config_key}", False).strip() or None

    def get_hooks_path(self) -> str:
        """
        Returns the path to the directory where Git hooks are stored, either
        from the Git configuration or the default location.
        """
        hooks_dir = self.get_config("core.hooksPath")
        if hooks_dir is None:
            hooks_dir = os.path.join(self.get_dot_git_path(), "hooks")
        return hooks_dir


class GitClient(GitReadonlyClient):
    """
    Client class that acts upon a git repository found in the process's current
    directory.
    """

    def init(self, main_branch: Union[str, None]):
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

    def stage(self, file_path: Union[str, None]):
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
