"""
check if a binary tree is a BST
"""

from TreeGraph.BST import *

def check_range(data, low, high):
    return low < data < high

def checkBST(node, x = -float('inf'), y = float('inf')):
    if node is None:
        return True
    else:
        isvalid = check_range(node.data, x, y)
        return isvalid and checkBST(node.leftnode, x, node.data) and checkBST(node.rightnode, node.data, y)


if __name__ == '__main__':
    x = [3, 4, 1, 2, 5]
    tree = BST(x[0])
    for i in range(1, len(x)):
        tree.insert(x[i])

    in_order(tree)

    print(checkBST(tree))
