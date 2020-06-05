"""
Tree traversal
"""
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data)
        in_order(node.right)


def pre_order(node):
    if node is not None:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data)

