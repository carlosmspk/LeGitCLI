from typing import Any
from model.exceptions import AbstractClassInstantiatedError


def prevent_abstract_instantiation(self: Any, abstract_type: type):
    if self.__class__ == abstract_type:
        raise AbstractClassInstantiatedError(self.__class__)
