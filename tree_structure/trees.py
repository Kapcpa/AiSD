# NODE CLASS


class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None


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
    print(f"Sorted: {" ".join([str(number) for number in data])}")
    tree: AVL = build_avl(data, 0, len(data) - 1)
    return tree


# SHARED FUNCTIONS


PRE_ORDER = 0
IN_ORDER = 1
POST_ORDER = 2
def traverse_tree(node: Node | None, order: int) -> list[int]:
    if not node:
        return []

    result = []

    result.append(node.key) if order == PRE_ORDER else None
    result += traverse_tree(node.left, order)
    result.append(node.key) if order == IN_ORDER else None
    result += traverse_tree(node.right, order)
    result.append(node.key) if order == POST_ORDER else None

    return result


def command_print(node: Node) -> Node:
    print(f"Pre-order: {" ".join([str(number) for number in traverse_tree(node, PRE_ORDER)])}")
    print(f"In-order: {" ".join([str(number) for number in traverse_tree(node, IN_ORDER)])}")
    print(f"Post-order: {" ".join([str(number) for number in traverse_tree(node, POST_ORDER)])}")
    return node


def command_help(node: Node) -> Node:
    print("Help: Show this message")
    print("Print: Prints the tree using Pre-order, In-order, Post-order")
    print("MinMax: Prints the min and max values in the tree")
    print("Delete: Removes specified nodes from the tree")
    print("DeleteAll: Removes the whole tree")
    print("Export: Exports the tree to a .txt file that can be fed into tikzpicture")
    print("Exit: Exits the program ( same as Ctrl + C )")

    return node


def min_node(node: Node) -> Node:
    node_min = node
    while node_min.left is not None:
        node_min = node_min.left
    return node_min


def max_node(node: Node) -> Node:
    node_max = node
    while node_max.right is not None:
        node_max = node_max.right
    return node_max


def command_min_max(node: Node) -> Node:
    print(f"Min: {min_node(node).key}")
    print(f"Max: {max_node(node).key}")

    return node


def tikz_format(node: Node) -> str:
    if not node.left and not node.right:
        return f"node {{{node.key}}}"

    left = f"child {{{tikz_format(node.left)}}}" if node.left else "child [missing]"
    right = f"child {{{tikz_format(node.right)}}}" if node.right else "child [missing]"

    return f"""node {{{node.key}}}\n{left}\n{right}"""


def command_export(node: Node) -> Node:
    file = open("tree.txt", "w")
    file.write("\\" + tikz_format(node) + ";")
    print("Tree exported.")

    return node


def delete_node(node: Node, key: int) -> Node:
    if not node:
        print(f"Value {key} doesn't exist in the tree.")
        return node

    if key < node.key:
        node.left = delete_node(node.left, key)
    elif key > node.key:
        node.right = delete_node(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left

        temp = max_node(node.left)
        node.key = temp.key
        node.left = delete_node(node.left, temp.key)

    return node


def command_delete(node: Node) -> Node:
    data: list[int] = [int(node) for node in input("nodes to delete> ").split()]
    for key in data:
        node = delete_node(node, key)

    return None


def command_delete_all(node: Node) -> Node:
    post_order_traverse = traverse_tree(node, POST_ORDER)
    print(f"Deleting: {" ".join([str(number) for number in post_order_traverse])}")
    for key in traverse_tree(node, POST_ORDER):
        delete_node(node, key)

    return node


def command_exit(*args) -> None:
    exit(0)
