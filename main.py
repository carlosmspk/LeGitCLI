from flows import Flows

def main():
    # TODO: Pick different flows depending on CLI verb (e.g. legit validate vs
    # legit config vs legit help)
    flow = Flows.VALIDATE
    flow()

if __name__ == "__main__":
    main()
