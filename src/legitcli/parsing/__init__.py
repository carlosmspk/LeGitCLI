from typing import List, Tuple
from legitcli.model.config import Config
from legitcli.model.ruleset import ScopedRuleset
import yaml
from legitcli.parsing.converters.legit_rules_converter import LegitRulesConverter
from legitcli.utils import LazyFileReader


def parse_legit_file(legit_file: LazyFileReader) -> Tuple[List[ScopedRuleset], Config]:
    yaml_data = yaml.safe_load(legit_file.read())
    return LegitRulesConverter(yaml_data).convert()
