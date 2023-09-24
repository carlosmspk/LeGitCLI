from model.command_configs import ErrorBehavior, OutputLevel


class GitReadonlyClient:
    """
    Client class that acts upon a git repository found in the process's current
    directory, but does not change the repository's state
    """

    def __init__(
        self,
        output_level: OutputLevel = OutputLevel.STANDARD,
        on_error: ErrorBehavior = ErrorBehavior.RAISE_EXCEPTION,
    ) -> None:
        self.__output_level: OutputLevel = output_level
        self.__on_error: ErrorBehavior = on_error

    def get_current_branch(self) -> str:
        """Returns the current active branch's name"""
        ...

    def get_author(self) -> tuple[str, str]:
        """
        Returns the configured user/author. Result is returned as tuple of name
        and email, respectively
        """
        ...
