from command import run_command
import os


class GitReadonlyClient:
    """
    Client class that acts upon a git repository found in the process's current
    directory, but does not change the repository's state
    """

    def get_current_branch(self) -> str:
        """Returns the current active branch's name"""
        return "develop"

    def get_author(self) -> tuple[str, str]:
        """
        Returns the configured user/author. Result is returned as tuple of name
        and email, respectively
        """
        return ("Author's Name", "author@mail.com")


class GitClient(GitReadonlyClient):
    """
    Client class that acts upon a git repository found in the process's current
    directory.
    """

    def init(self, main_branch: str):
        """Initializes a git repository at current directory. Accepts an initial
        main branch name (default: 'main')"""
        ...

    def commit(self, message: str):
        """
        Commits staged changes with `message`.

        Raises an exception if commit fails, e.g. because there are no staged
        files or message is invalid.

        Mutating method: calling this method will raise an exception if this
        client instance is set as readonly
        """
        ...

    def stage(self, file_path: str):
        """
        Stages `file_path` for committing.

        Raises an exception if stage fails, e.g. because file does not exist or
        has no changes.

        Mutating method: calling this method will raise an exception if this
        client instance is set as readonly
        """
        ...
