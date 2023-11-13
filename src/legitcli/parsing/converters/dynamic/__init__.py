from dataclasses import fields
from typing import Any, List
from legitcli.model.exceptions import (
    UnknownLegitEntityTypeError,
)
from legitcli.model.rules import Rule
from legitcli.model.bindings import rule_bindings_map, scope_bindings_map
from legitcli.model.scope_conditions import ScopeCondition, ScopeConditionAction
from legitcli.parsing.converters.base_converter import BaseConverter


def _snake_to_pascal(s):
    return "".join(part.capitalize() for part in s.split("_"))


class ConcreteRuleParametersConverter(BaseConverter[dict, Rule]):
    def __init__(
        self, object_to_convert: dict, field_path: List[str], rule_type: str
    ) -> None:
        super().__init__(object_to_convert, field_path, dict)
        if rule_type not in rule_bindings_map:
            print([i for i in rule_bindings_map])
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


class ConcreteScopeConditionParametersConverter(BaseConverter[dict, ScopeCondition]):
    def __init__(
        self,
        object_to_convert: dict,
        field_path: List[str],
        scope_action: str,
        scope_type: str,
    ) -> None:
        super().__init__(object_to_convert, field_path, dict)
        if scope_type not in scope_bindings_map:
            raise UnknownLegitEntityTypeError(
                entity="Scope Condition", unknown_entity_name=scope_type
            )
        self.ScopeConditionDataclass = scope_bindings_map[scope_type]
        self.scope_action = self._get_action_enum_from_string(scope_action)

    def convert(self) -> ScopeCondition:
        field_values: dict[str, Any] = {"action": self.scope_action}

        field_names = {
            field.name: _snake_to_pascal(field.name)
            for field in fields(self.ScopeConditionDataclass)
            if field.name != "action"
        }

        self._assert_fields(required_field_names=set(field_names.values()))

        field_values = {
            param_python_name: self.object_to_convert[param_yaml_name]
            for param_python_name, param_yaml_name in field_names.items()
        }
        return self.ScopeConditionDataclass(action=self.scope_action, **field_values)

    def _get_action_enum_from_string(self, action_str: str) -> ScopeConditionAction:
        for action in ScopeConditionAction:
            if action.value == action_str:
                return action
        raise ValueError(f"Invalid value for Action: '{action_str}'")
