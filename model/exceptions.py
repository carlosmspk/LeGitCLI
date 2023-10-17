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
