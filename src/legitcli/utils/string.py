import re
from typing import Dict, List, Union
from legitcli.utils.lazy import Lazy


def replace_params(
    string: str, param_value_map: Dict[str, Union[Lazy[str], str]]
) -> str:
    pattern = re.compile(r"\{(\w+)\}")
    matches: List[str] = re.findall(pattern, string)

    for param_name in matches:
        try:
            param_value = param_value_map[param_name]
            if isinstance(param_value, Lazy):
                param_value = param_value.get()
            string = string.replace(f"{{{param_name}}}", param_value)
        except KeyError:
            pass

    return string
