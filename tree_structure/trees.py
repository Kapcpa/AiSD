class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None


class BST(Node):
    ...


class AVL(Node):
    def __init__(self, key: int):
        super().__init__(key)
        self.height: int = 1


def insert_bst(root: BST | None, key: int) -> BST:
    if not root:
        return BST(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root


PRE_ORDER = 0
IN_ORDER = 1
POST_ORDER = 2
def print_tree(node: Node | None, order: int) -> None:
    if not node:
        return
    print(node.key, end=" ")    if order == PRE_ORDER else None
    print_tree(node.left, order)
    print(node.key, end=" ")    if order == IN_ORDER else None
    print_tree(node.right, order)
    print(node.key, end=" ")    if order == POST_ORDER else None


def command_print(node: Node) -> None:
    print("Pre-order: ", end="")
    print_tree(node, PRE_ORDER)
    print("\nIn-order: ", end="")
    print_tree(node, IN_ORDER)
    print("\nPost-order: ", end="")
    print_tree(node, POST_ORDER)
    print("")


def command_help(*args) -> None:
    print("Help:\tShow this message")
    print("Print:\tPrints the tree using Pre-order, In-order, Post-order")
    print("MinMax:\tPrints the min and max values in the tree")
    print("Export:\tExports the tree to a .txt file that can be fed into tikzpicture")
    print("Exit:\tExits the program ( same as Ctrl + C )")


def command_min_max(node: Node) -> None:
    node_min = node
    while node_min.left is not None:
        node_min = node_min.left
    print(f"Min: {node_min.key}")

    node_max = node
    while node_max.right is not None:
        node_max = node_max.right
    print(f"Max: {node_max.key}")


def tikz_format(node: Node) -> str:
    if not node.left and not node.right:
        return f"node {{{node.key}}}"

    left = f"child {{{tikz_format(node.left)}}}" if node.left else "child [missing]"
    right = f"child {{{tikz_format(node.right)}}}" if node.right else "child [missing]"

    return f"""node {{{node.key}}}\n{left}\n{right}"""


def command_export(node: Node):
    file = open("tree.txt", "w")
    file.write("\\" + tikz_format(node) + ";")
    print("Tree exported.")


def command_exit(*args) -> None:
    exit(0)
