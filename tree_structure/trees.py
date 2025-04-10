# NODE CLASS


class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None


# BST FUNCTIONS


class BST(Node):
    ...


def insert_bst(root: BST | None, key: int) -> BST:
    if not root:
        return BST(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root


def build_bst(data: list[int]) -> BST:
    tree: BST = None
    for key in data:
        tree = insert_bst(tree, key)
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


def insert_avl(data: list[int], start: int, end: int) -> AVL:
    if start > end:
        return None

    mid = (start + end) // 2
    node = AVL(data[mid])

    node.left = insert_avl(data, start, mid - 1)
    node.right = insert_avl(data, mid + 1, end)

    return balance(node)


def build_avl(data: list[int]) -> AVL:
    data = sorted(data)
    print(f"Sorted: {" ".join([str(number) for number in data])}")
    tree: AVL = insert_avl(data, 0, len(data) - 1)
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
