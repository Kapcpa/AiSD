"""
TODO:
- visualiser / export command
- correct tree initializations (AVL)
- commands implementation:
    - Find Max, Min, MinMax
    - remove
    - rebalance
    - delete
- cleaning up the code - try putting tree-specific implementations under correct classes,
    and if the implementation works for both put it in the parent-class
- maybe change the way the data is fed in (no need for nodes> actually...)

"""


import sys
from trees import *


tree_types = {
    "AVL", 
    "BST"
}


commands = {
    "Help": command_help,
    "Print": command_print,
    "Exit": command_exit
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
        nodes = int(input("nodes> "))
        data = [int(node) for node in input("insert> ").split()]
        if len(data) == nodes:
            break
        print("ERROR: Declared amount of nodes does not match the data passed in")
    
    tree: Node = None
    for key in data:
        tree = insert_bst(tree, key)

    while True:
        action = input("action> ")
        if action not in commands:
            print("ERROR: Invalid action. Type 'Help' to see possible actions")
            continue
        print(action)
        commands[action](tree)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        command_exit()
