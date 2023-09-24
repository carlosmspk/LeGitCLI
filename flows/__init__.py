from enum import Enum
from typing import Callable
import flows.validate as validate


class Flows(Enum):
    VALIDATE = validate.run_flow

    @staticmethod
    def get(key: str) -> Callable[[], None]:
        """Get flow function from key. If key can't be found, returns
        default 'help' flow. Key value is not case sensitive"""
        key, default = key.upper(), default.upper()
        self_dict = {
            name: value
            for name, value in filter(lambda x: x[0].isupper(), Flows.__dict__.items())
        }
        return self_dict.[key]

    @staticmethod
    def get_flow_names() -> list[str]:
        """Returns a list of all flow variants' names, lower cased."""
        return {name.lower() for name in filter(str.isupper, Flows.__dict__)}
