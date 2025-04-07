import sys


tree_types = {
    "AVL", 
    "BST"
}


def main():
    # Command-line arguments: python main.py --tree <tree-type>
    if len(sys.argv) != 3 or sys.argv[1] != "--tree" or sys.argv[2] not in tree_types:
        print("Usage: python3 main.py --tree <tree-type>")
        print("<tree-type> AVL or BST")
        sys.exit(1)

    nodes: int | None = None
    data: list[int] = []

    while True:
        nodes = int(input("nodes>"))
        data = [int(node) for node in input("insert>").split()]
        if len(data) == nodes:
            break
        print("ERROR: Declared amount of nodes does not match the data passed in")
    
    # input = sys.stdin.read().split()
    # try:
    #     data = [int(x) for x in input]
    # except EOFError:
    #     print("Error reading input.")


    # Print the unsorted data
    # print(f"Unsorted data: {log_data(data)}")

    # Executes the sorting function that corresponds to the algorithm_id

    # Print the sorted data


if __name__ == "__main__":
    main()
