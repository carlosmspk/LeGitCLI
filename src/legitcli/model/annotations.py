from legitcli.model.bindings import rule_bindings_map, scope_bindings_map
from legitcli.model.exceptions import RedefinedEntityTypeBindingError


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


def scope_condition_binds_to_type(scope_condition_type_name: str):
    """Binds this ScopeCondition dataclass to `scope_condition_type_name` such
    that, in YAML, a ScopeCondition whose Type field matches
    `scope_condition_type_name` will automatically be converted to a scope
    condition of this dataclass"""

    def decorator(cls):
        if scope_condition_type_name in scope_bindings_map:
            raise RedefinedEntityTypeBindingError(
                entity="Rule",
                redefined_type=scope_condition_type_name,
                previously_defined_type=scope_bindings_map[scope_condition_type_name],
                attempted_to_define_type=cls,
            )
        scope_bindings_map[scope_condition_type_name] = cls
        return cls

    return decorator
