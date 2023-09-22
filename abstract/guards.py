from typing import Any
from model.exceptions import IllegalAbstractClassInitCall


def prevent_abstract_instantiation(self: Any, abstract_type: type):
    if self.__class__ == abstract_type:
        raise IllegalAbstractClassInitCall(self.__class__)
