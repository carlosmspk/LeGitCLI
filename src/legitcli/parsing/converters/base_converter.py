from typing import Generic, TypeVar, List, Set
from legitcli.typeutils import guards
from legitcli.model.exceptions import LeGitRulesMissingYamlFieldError

O = TypeVar("O")
I = TypeVar("I", dict, list)


class BaseConverter(Generic[I, O]):
    """Pseudo-abstract base class for Converters, which takes in"""

    def __init__(
        self, object_to_convert: I, field_path: List[str], expected_type: type
    ) -> None:
        guards.prevent_abstract_instantiation(self, BaseConverter)
        guards.assert_type(object_to_convert, expected_type, ">".join(field_path))
        self.field_path = field_path
        self.object_to_convert: I = object_to_convert

    def convert(self) -> O:
        raise NotImplementedError("abstract method 'parse' is meant to be overriden")

    def _assert_fields(
        self,
        required_field_names: Set[str] = set(),
        optional_field_names: Set[str] = set(),
    ):
        known_field_names = required_field_names.union(optional_field_names)

        for field_name in required_field_names:
            if field_name not in self.object_to_convert:
                raise LeGitRulesMissingYamlFieldError(
                    required_field_name=field_name, field_path=self.field_path
                )

        for field_name in self.object_to_convert:
            if field_name not in known_field_names:
                print(
                    f"WARN: Ignoring unknown field '{field_name}' at {'>'.join(self.field_path)}"
                )
