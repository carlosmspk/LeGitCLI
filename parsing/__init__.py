from model.config import Config
from model.ruleset import ScopedRuleset
import yaml
from parsing.converters.legit_rules_converter import LegitRulesConverter


def parse_legit_file(legit_file_path: str) -> tuple[list[ScopedRuleset], Config]:
    with open(legit_file_path, "r") as f:
        yaml_data = yaml.safe_load(f)
    return LegitRulesConverter(yaml_data).convert()
