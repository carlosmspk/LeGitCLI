from typing import Any
from legitcli.model.exceptions import AbstractClassInstantiatedError


def prevent_abstract_instantiation(self: Any, abstract_type: type):
    if self.__class__ == abstract_type:
        raise AbstractClassInstantiatedError(self.__class__)


def assert_type(target_object: object, target_type: type, target_name: str):
    if not isinstance(target_object, target_type):
        raise TypeError(
            f"Expected object '{target_name}' to be of type or subclass of '{target_type}' but found it to be of type '{type(target_object)}'"
        )
