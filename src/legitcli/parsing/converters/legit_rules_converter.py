from typing import List, Tuple
from legitcli.model.scope_conditions import (
    AlwaysTrueScopeCondition,
    ScopeConditionAction,
)
from legitcli.parsing.converters.base_converter import BaseConverter
from legitcli.parsing.converters.config_converter import ConfigConverter
from legitcli.model.config import Config
from legitcli.model.ruleset import ScopedRuleset
from legitcli.parsing.converters.rule_converter import RuleConverter
from legitcli.parsing.converters.scoped_ruleset_converter import ScopedRulesetConverter


class LegitRulesConverter(BaseConverter[dict, Tuple[List[ScopedRuleset], Config]]):
    def __init__(self, legit_rules_dict: dict) -> None:
        super().__init__(legit_rules_dict, ["<root>"], dict)

    def convert(self) -> Tuple[List[ScopedRuleset], Config]:
        self._assert_fields(
            optional_field_names={"Config", "ScopedRules", "GenericRules"}
        )
        config = self._convert_config()
        converted_scoped_ruleset_list = self._convert_scoped_ruleset()
        self._convert_generic_rules_and_append_to_scoped_ruleset(
            converted_scoped_ruleset_list
        )

        return (converted_scoped_ruleset_list, config)

    def _convert_config(self) -> Config:
        raw_config_dict: dict = self.object_to_convert.get("Config", {})
        config = ConfigConverter(raw_config_dict, ["Config"]).convert()
        return config

    def _convert_scoped_ruleset(self) -> List[ScopedRuleset]:
        raw_scoped_ruleset_list: list = self.object_to_convert.get("ScopedRules", [])
        converted_scoped_ruleset_list = []
        for nth, raw_ruleset in enumerate(raw_scoped_ruleset_list):
            prased_scoped_ruleset = ScopedRulesetConverter(
                raw_ruleset, ["ScopedRules", f"[{nth}]"]
            ).convert()
            converted_scoped_ruleset_list.append(prased_scoped_ruleset)
        return converted_scoped_ruleset_list

    def _convert_generic_rules_and_append_to_scoped_ruleset(
        self, converted_scoped_ruleset_list
    ):
        raw_generic_rules_list = self.object_to_convert.get("GenericRules", [])
        converted_generic_rules_list = []
        for nth, rule_dict in enumerate(raw_generic_rules_list):
            rule = RuleConverter(rule_dict, ["GenericRules", f"[{nth}]"]).convert()
            converted_generic_rules_list.append(rule)
        if len(converted_generic_rules_list) > 0:
            generic_rules_ruleset = ScopedRuleset(
                [AlwaysTrueScopeCondition(action=ScopeConditionAction.INCLUDE)],
                converted_generic_rules_list,
            )
            converted_scoped_ruleset_list.insert(0, generic_rules_ruleset)
