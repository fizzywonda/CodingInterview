"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""

"""
with link to the parents
"""
from TreeGraph.MinimalTree import Node

def first_common_ancestor1(root, node_a, node_b):
    diff = depth(node_a) - depth(node_b)
    # first = None
    # second = None

    if diff >= 0:
        first = node_a
        second = node_b
    else:
        first = node_b
        second = node_a

    first = move_up(first, abs(diff))

    while first != second:
        first = first.parent
        second = second.parent

    return first

def move_up(node, d):

    if d == 0:
        return node

    while d > 0:
        node = node.parent
        d -= 1
    return node


def depth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.parent
    return d

"""
when there's no link to the parent
"""

def first_common_ancestor2(root, node_a, node_b):
    if covers(root, node_a) and covers(root, node_b):
        return first_ancestor_helper(root, node_a, node_b)


def first_ancestor_helper(root, node_a, node_b):

    left_a = covers(root.left_child, node_a)
    left_b = covers(root.left_child, node_b)

    if left_a != left_b:
        return root
    if left_a:
        return first_ancestor_helper(root.left_child, node_a, node_b)
    else:
        return first_ancestor_helper(root.right_child, node_a, node_b)


def covers(root, node):    # check if a node is in a subtree of a root.
    if root is None:
        return False
    if root == node:
        return True
    if covers(root.left_child, node) or covers(root.right_child, node):
        return True

if __name__ == '__main__':
    a = Node(4)
    b = Node(2)
    c = Node(5)
    d = Node(1)
    e = Node(3)
    f = Node(6)

    a.left_child = b
    a.right_child = c
    b.left_child = d
    b.right_child = e
    b.parent = a
    c.parent = a
    c.right_child = f
    d.parent = b
    e.parent = b
    f.parent = c

    x = first_common_ancestor1(a, e, c)
    print(x.data)