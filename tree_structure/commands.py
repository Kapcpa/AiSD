from trees import *


def command_print(node: Node) -> Node:
    print(f"Pre-order: {" ".join([str(number) for number in traverse_tree(node, PRE_ORDER)])}")
    print(f"In-order: {" ".join([str(number) for number in traverse_tree(node, IN_ORDER)])}")
    print(f"Post-order: {" ".join([str(number) for number in traverse_tree(node, POST_ORDER)])}")
    return node


def command_help(node: Node) -> Node:
    print("Help: Show this message")
    print("Print: Prints the tree using Pre-order, In-order, Post-order")
    print("MinMax: Prints the min and max values in the tree")
    print("Rebalance: Rebalances the tree using DSW method")
    print("Delete: Removes specified nodes from the tree")
    print("DeleteAll: Removes the whole tree")
    print("Export: Exports the tree to a .txt file that can be fed into tikzpicture")
    print("Exit: Exits the program ( same as Ctrl + C )")

    return node


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


def command_rebalance(node: Node) -> Node:
    return node
