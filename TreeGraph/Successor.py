"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""
from TreeGraph.MinimalTree import Node

class Node1(Node):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None

def successor(node):
    if node is None:
        return None
    if node.right_child is not None:
        return get_left_most_child(node.right)
    else:
        q = node.parent
        while q is not None and q.left_child != node:
            node = q
            q = q.parent
        return q



def get_left_most_child(node):
    while node.left is not None:
        node = node.left
    return node

if __name__ == '__main__':
    a = Node1(4)
    b = Node1(2)
    c = Node1(5)
    d = Node1(1)
    e = Node1(3)

    a.left_child = b
    a.right_child = c
    b.left_child = d
    b.right_child = e
    b.parent = a
    c.parent = a
    d.parent = b
    e.parent = b

    print(successor(e).data)