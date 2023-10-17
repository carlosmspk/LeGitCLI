from dataclasses import fields
from model.exceptions import UnknownLegitEntityTypeError
from model.rules import Rule
from model.bindings import rule_bindings_map
from parsing.converters.base_converter import BaseConverter


def _snake_to_pascal(s: str) -> str:
    return "".join(part.capitalize() for part in s.split("_"))


class ConcreteRuleParametersConverter(BaseConverter[dict, Rule]):
    def __init__(
        self, object_to_convert: dict, field_path: list[str], rule_type: str
    ) -> None:
        super().__init__(object_to_convert, field_path, dict)
        if rule_type not in rule_bindings_map:
            raise UnknownLegitEntityTypeError(
                entity="Rule", unknown_entity_name=rule_type
            )
        self.RuleDataclass = rule_bindings_map[rule_type]

    def convert(self) -> Rule:
        field_names = {
            field.name: _snake_to_pascal(field.name)
            for field in fields(self.RuleDataclass)
        }

        self._assert_fields(required_field_names=set(field_names.values()))

        field_values = {
            param_python_name: self.object_to_convert[param_yaml_name]
            for param_python_name, param_yaml_name in field_names.items()
        }
        return self.RuleDataclass(**field_values)
