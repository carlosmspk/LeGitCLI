from typing import Union


class LazyFileReader:
    def __init__(self, file_path: str) -> None:
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Could not find required file '{file_path}'")
        self.__file_path = file_path
        self.__content: Union[str, None] = None

    def read(self) -> str:
        if self.__content is None:
            with open(self.__file_path, "r") as f:
                self.__content = f.read()
        return self.__content
