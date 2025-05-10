import sys
from trees import *
from commands import *


tree_init = {
    "AVL": build_avl, 
    "BST": build_bst
}


commands = {
    "Help": command_help,
    "Print": command_print,
    "MinMax": command_min_max,
    "Rebalance": command_rebalance,
    "Delete": command_delete,
    "DeleteAll": command_delete_all,
    "Export": command_export,
    "Exit": command_exit
}

# func = globals()["MinMax"]
# func()

def main():
    # Command-line arguments: python main.py --tree <tree-type>
    if len(sys.argv) != 3 or sys.argv[1] != "--tree" or sys.argv[2] not in tree_init:
        print("Usage: python3 main.py --tree <tree-type>")
        print("<tree-type> 'AVL' or 'BST'")
        sys.exit(1)

    data: list[int] = [int(node) for node in input("insert> ").split()]
    
    tree_type = sys.argv[2]
    tree: Node = tree_init[tree_type](data)

    while True:
        action = input("action> ").strip()
        if action not in commands:
            print("ERROR: Invalid action. Type 'Help' to see possible actions.")
            continue
        elif tree is None and action != "Exit":
            print("ERROR: Can't perform this action because the tree has been removed.")
            continue
        tree = commands[action](tree)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        command_exit()
