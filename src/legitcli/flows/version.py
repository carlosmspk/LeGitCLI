import importlib.metadata
from typing import List


def run_flow(args: List[str]):
    print(f"LeGit CLI {importlib.metadata.version('legitcli')}")
