import sys


graph_init = {
    "--generate": None,
    "--user-provided": None
}

commands = {

}


def main():
    # Command-line arguments: python3 main.py --graphs <input-type>
    if len(sys.argv) != 3 or sys.argv[1] != "--graph" or sys.argv[2] not in graph_init:
        print("Usage: python3 main.py --graphs <input-type>")
        print("<input-type> '--generate' or '--user-provided'")
        sys.exit(1)

    while True:
        action = input("action> ").strip()
        if action not in commands:
            print("ERROR: Invalid action. Type 'Help' to see possible actions.")
            continue

        ...


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
