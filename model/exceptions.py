class IllegalAbstractClassInitCall(Exception):
    """Attempted to instantiate an abstract class"""

    def __init__(self, abstract_class_type: type) -> None:
        super().__init__(
            f"Cannot instantiate Abstract class '{abstract_class_type.__name__}' directly."
        )
