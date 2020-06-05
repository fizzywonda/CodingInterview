"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.parent = None

    def get_children(self):
        return [self.left_child, self.right_child]


def minimal_tree(arr):
    return minimal_tree(arr, 0, len(arr) - 1)


def minimal_tree(arr, start, end):
    if start < end:
        return None
    else:
        mid = (start + end)/2
        parent = Node(arr[mid])
        parent.right_child = minimal_tree(arr, start, mid - 1)
        parent.left_child = minimal_tree(arr, mid + 1, end)
        return parent

