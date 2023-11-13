from typing import List, Tuple
from model.config import Config
from model.ruleset import ScopedRuleset
import yaml
from parsing.converters.legit_rules_converter import LegitRulesConverter
from utils import LazyFileReader


def parse_legit_file(legit_file: LazyFileReader) -> Tuple[List[ScopedRuleset], Config]:
    yaml_data = yaml.safe_load(legit_file.read())
    return LegitRulesConverter(yaml_data).convert()
