# SHARED FUNCTIONS


class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None


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


# BST FUNCTIONS


class BST(Node):
    ...


def build_bst(root: BST | None, key: int) -> BST:
    if not root:
        return BST(key)
    if key < root.key:
        root.left = build_bst(root.left, key)
    else:
        root.right = build_bst(root.right, key)
    return root


def insert_bst(data: list[int]) -> BST:
    tree: BST = None
    for key in data:
        tree = build_bst(tree, key)
    return tree


# AVL FUNCTIONS


class AVL(Node):
    def __init__(self, key: int):
        super().__init__(key)
        self.height: int = 1


def height(node: AVL) -> int:
    return node.height if node else 0


def get_balance(node: AVL) -> int:
    return height(node.left) - height(node.right) if node else 0


def update_height(node: AVL) -> None:
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_right(node: AVL) -> AVL:
    other = node.left
    T2 = other.right

    other.right = node
    node.left = T2

    update_height(node)
    update_height(other)

    return other


def rotate_left(node: AVL) -> AVL:
    other = node.right
    T2 = other.left

    other.left = node
    node.right = T2

    update_height(node)
    update_height(other)

    return other


def balance(node: AVL) -> AVL:
    update_height(node)
    branch_balance = get_balance(node)

    if branch_balance > 1:
        if get_balance(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    if branch_balance < -1:
        if get_balance(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


def build_avl(data: list[int], start: int, end: int) -> AVL:
    if start > end:
        return None

    mid = (start + end) // 2
    node = AVL(data[mid])

    node.left = build_avl(data, start, mid - 1)
    node.right = build_avl(data, mid + 1, end)

    return balance(node)


def insert_avl(data: list[int]) -> AVL:
    data = sorted(data)
    tree: AVL = build_avl(data, 0, len(data) - 1)
    return tree
