"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
import sys
from TreeGraph.MinimalTree import Node

def validate_bst(node):

    return validate_bst2(node, None, None)

def validate_bst2(node, min, max):
    if node == None:
        return True
    if (min is not None and node.data < min) or (max is not None and node.data > max):
        return False

    if not validate_bst2(node.left_child, min, node.data) or not validate_bst2(node.right_child, node.data, max):
        return False
    return True

"""
using an in_order traversal method

Noted: it does not work for bst with duplicate values
"""

def validate(node):
    arr = []
    def in_order(node):
        if node is not None:
            in_order(node.left_child)
            arr.append(node.data)
            in_order(node.right_child)

    in_order(node)
    for i in range(1, len(arr)):
        if arr[i] <= arr[i -1]:
            return False
    return True

""" testing def within a def"""
def print1():
    a = " world"
    def print2():
        print("hello" + a)
    print2()
print1()

if __name__ == '__main__':
    a = Node(4)
    b = Node(2)
    c = Node(5)
    d = Node(1)
    e = Node(3)

    a.left_child = b
    a.right_child = c
    b.left_child = d
    b.right_child = e

    x = validate_bst(a)
    print(x)