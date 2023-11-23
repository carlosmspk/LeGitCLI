from legitcli.git.client import GitReadonlyClient as __Git
from legitcli.utils.lazy import Lazy as __Lazy


parameter_value_map = {"AUTHOR": __Lazy(lambda: __Git().get_author()[0])}
