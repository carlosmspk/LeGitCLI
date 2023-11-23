from typing import Generic, TypeVar, Union, Callable


T = TypeVar("T")


class Lazy(Generic[T]):
    def __init__(self, callback: Callable[..., T]) -> None:
        self.__value: Union[T, None] = None
        self.__callback: Union[Callable[..., T], None] = callback

    def get(self) -> T:
        if self.__callback is None:
            return self.__value
        self.__value = self.__callback()
        self.__callback = None
        return self.__value


class LazyFileReader(Lazy[str]):
    def __read_file_callback(file_path: str):
        with open(file_path, "r") as f:
            return f.read()

    def __init__(self, file_path: str) -> None:
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Could not find required file '{file_path}'")
        super().__init__(lambda: LazyFileReader.__read_file_callback(file_path))
