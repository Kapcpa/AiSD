class BST:
    def __init__(self, key: int):
        self.key: int = key
        self.left: BST | None = None
        self.right: BST | None = None


def insert_bst(root: BST | None, key: int) -> BST:
    if not root:
        return BST(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

