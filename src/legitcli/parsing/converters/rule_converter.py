from typing import List
from legitcli.model.rules import Rule
from legitcli.parsing.converters.base_converter import BaseConverter
from legitcli.parsing.converters.dynamic import ConcreteRuleParametersConverter


class RuleConverter(BaseConverter[dict, Rule]):
    def __init__(self, rule_dict: dict, field_path: List[str]) -> None:
        super().__init__(rule_dict, field_path, dict)

    def convert(self) -> Rule:
        self._assert_fields(required_field_names={"Type", "Parameters"})
        rule_type = self.object_to_convert["Type"]
        rule_parameters = self.object_to_convert["Parameters"]

        return ConcreteRuleParametersConverter(
            rule_parameters, self.field_path + ["Parameters"], rule_type
        ).convert()
