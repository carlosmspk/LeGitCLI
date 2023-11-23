import sys
from legitcli.flows import Flows


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("ERROR: Missing verb\n")
        Flows.HELP([])
        exit(1)
    _, verb, *args = sys.argv
    flow = Flows.get(verb)
    flow(args)


if __name__ == "__main__":
    main()
