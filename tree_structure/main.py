"""
TODO:
- AVL tree
- commands implementation:
    - remove
    - rebalance
    - delete
- cleaning up the code - try putting tree-specific implementations under correct classes,
    and if the implementation works for both put it in the parent-class
- make it so it works with heredoc better ??? (tho i think it does work)

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
    "MinMax": command_min_max,
    "Export": command_export,
    "Exit": command_exit
}


def main():
    # Command-line arguments: python main.py --tree <tree-type>
    if len(sys.argv) != 3 or sys.argv[1] != "--tree" or sys.argv[2] not in tree_types:
        print("Usage: python3 main.py --tree <tree-type>")
        print("<tree-type> 'AVL' or 'BST'")
        sys.exit(1)

    data: list[int] = [int(node) for node in input("insert> ").split()]
    
    tree: Node = None
    for key in data:
        tree = insert_bst(tree, key)

    while True:
        action = input("action> ")
        if action not in commands:
            print("ERROR: Invalid action. Type 'Help' to see possible actions.")
            continue
        commands[action](tree)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        command_exit()
