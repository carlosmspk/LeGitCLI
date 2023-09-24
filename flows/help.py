def run_flow():
    from flows import Flows

    valid_legit_verbs = "\n".join("\t- " + i for i in Flows.get_flow_names())
    print(
        "Command usage:",
        "\tlegit <verb> [args]",
        "valid verbs:",
        valid_legit_verbs,
        sep="\n",
    )
