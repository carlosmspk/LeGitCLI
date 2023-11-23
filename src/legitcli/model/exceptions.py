from typing import Iterable


class AbstractClassInstantiatedError(Exception):
    """Attempted to instantiate an abstract class"""

    def __init__(self, abstract_class_type: type) -> None:
        super().__init__(
            f"Cannot instantiate Abstract class '{abstract_class_type.__name__}' directly."
        )


class LeGitRulesMissingYamlFieldError(Exception):
    """Parsed LeGit file does not have expected field"""

    def __init__(self, required_field_name: str, field_path: Iterable[str]) -> None:
        super().__init__(
            f"Missing required field '{required_field_name}' at '{' > '.join(field_path)} > {required_field_name}'"
        )


class RedefinedEntityTypeBindingError(Exception):
    """Annotated two different entities to bind to the same target"""

    def __init__(
        self,
        entity: str,
        redefined_type: str,
        previously_defined_type: type,
        attempted_to_define_type: type,
    ) -> None:
        super().__init__(
            f"Attempted to redefine {entity}'s bind target '{redefined_type}' on class '{attempted_to_define_type.__name__}' but this target was already assigned to class '{previously_defined_type.__name__}'"
        )


class UnknownLegitEntityTypeError(Exception):
    """Found rule or scope condition type name that was not bound to a concrete rule or scope condition dataclass"""

    def __init__(self, entity: str, unknown_entity_name: str) -> None:
        super().__init__(
            f"Unknown {entity} type: '{unknown_entity_name}'. Either this {entity} has a typo, or no dataclass exists with the approppriate binding annotation."
        )
