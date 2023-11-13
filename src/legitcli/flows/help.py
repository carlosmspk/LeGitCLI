from typing import List


def run_flow(args: List[str]):
    """This flow prints out legit usage and returns"""
    from legitcli.flows import Flows

    valid_legit_verbs = "\n".join("\t- " + i for i in Flows.get_flow_names())
    print(
        "Command usage:",
        "\tlegit <verb> [args]",
        "Valid verbs:",
        valid_legit_verbs,
        sep="\n",
    )
