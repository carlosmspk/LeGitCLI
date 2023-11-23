from typing import List
from legitcli.model.ruleset import ScopedRuleset
from legitcli.parsing.converters.base_converter import BaseConverter
from legitcli.parsing.converters.rule_converter import RuleConverter
from legitcli.parsing.converters.scope_condition_converter import (
    ScopeConditionConverter,
)


class ScopedRulesetConverter(BaseConverter[dict, ScopedRuleset]):
    def __init__(self, scoped_ruleset: dict, field_path: List[str]) -> None:
        super().__init__(scoped_ruleset, field_path, dict)

    def convert(self) -> ScopedRuleset:
        self._assert_fields(required_field_names={"Scope", "Rules", "Name"})
        scoped_ruleset_name = self.object_to_convert["Name"]
        converted_rule_list = self._convert_rules()
        converted_scope_condition_list = self._convert_scope_conditions()

        return ScopedRuleset(
            scoped_ruleset_name, converted_scope_condition_list, converted_rule_list
        )

    def _convert_scope_conditions(self):
        converted_scope_condition_list = []
        for nth, raw_scope_condition in enumerate(self.object_to_convert["Scope"]):
            converted_scope_condition = ScopeConditionConverter(
                raw_scope_condition, self.field_path + ["Scope", f"[{nth}]"]
            ).convert()
            converted_scope_condition_list.append(converted_scope_condition)
        return converted_scope_condition_list

    def _convert_rules(self):
        converted_rule_list = []
        for nth, raw_rule in enumerate(self.object_to_convert["Rules"]):
            converted_rule = RuleConverter(
                raw_rule, self.field_path + ["Rules", f"[{nth}]"]
            ).convert()
            converted_rule_list.append(converted_rule)
        return converted_rule_list
