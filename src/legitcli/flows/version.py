import importlib.metadata
from typing import List


def run_flow(args: List[str]):
    try:
        print(importlib.metadata.version("legitcli"))
    except importlib.metadata.PackageNotFoundError:
        # Handle the case where the package is not installed
        print("unknown")
