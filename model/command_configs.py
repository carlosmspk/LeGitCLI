from enum import Enum, auto


class OutputLevel(Enum):
    """Controls output of executed commands"""
    STANDARD = ""
    """prints standard output and error to terminal"""
    SILENT = auto()
    """prints error to terminal"""
    NO_OUTPUT = auto()
    """does not print to terminal"""


class ErrorBehavior(Enum):
    RAISE_EXCEPTION = auto()
    """Raises exception immediately for non-zero exit codes."""
    RETURN_NONE = auto()
    """Returns `None` value immediately for non-zero exit codes."""