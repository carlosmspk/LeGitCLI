from model.bindings import (
    rule_bindings_map,
)
from model.exceptions import RedefinedEntityTypeBindingError


def rule_binds_to_type(rule_type_name: str):
    """Binds this Rule dataclass to `rule_type_name` such that, in YAML, a Rule
    whose Type field matches `rule_type_name` will automatically be converted to
    a rule of this dataclass"""

    def decorator(cls):
        if rule_type_name in rule_bindings_map:
            raise RedefinedEntityTypeBindingError(
                entity="Rule",
                redefined_type=rule_type_name,
                previously_defined_type=rule_bindings_map[rule_type_name],
                attempted_to_define_type=cls,
            )
        rule_bindings_map[rule_type_name] = cls
        return cls

    return decorator
