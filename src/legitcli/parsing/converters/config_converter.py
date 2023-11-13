from typing import List
from legitcli.model.config import Config
from legitcli.parsing.converters.base_converter import BaseConverter


class ConfigConverter(BaseConverter[dict, Config]):
    def __init__(self, object_to_convert: dict, field_path: List[str]) -> None:
        super().__init__(object_to_convert, field_path, dict)

    def convert(self) -> Config:
        return Config()
