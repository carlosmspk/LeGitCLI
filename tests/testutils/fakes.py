from typing import Tuple, Union
from legitcli.git.client import GitReadonlyClient
from legitcli.utils.lazy import LazyFileReader


class FakeLazyFileReader(LazyFileReader):
    def __init__(self, returned_string) -> None:
        self.returned_string = returned_string

    def get(self) -> str:
        return self.returned_string


class FakeGitReadonlyClient(GitReadonlyClient):
    def __init__(self) -> None:
        self.current_branch = None
        self.author = None
        self.dot_git_path = "."
        self.git_hooks_path = "."
        self.configs = {}

    def get_current_branch(self) -> str:
        return self.current_branch

    def get_author(self) -> Tuple[Union[str, None], Union[str, None]]:
        return self.author

    def get_dot_git_path(self) -> str:
        return self.dot_git_path

    def get_config(self, config_key: str) -> Union[str, None]:
        return self.configs.get(config_key, None)

    def get_hooks_path(self) -> str:
        return self.git_hooks_path
