"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
from TreeGraph.MinimalTree import Node
root = Node()


def check_balance_tree(root):
    if root.get_children() is None:
        return 0
    height = []
    for n in root.get_children():
        if n.visited == False:
            n.visited = True
        curr_height = 1 + check_balance_tree(n)
        height.append(curr_height)
    if abs(height[0] - height[1]) > 1:
        return False
    else:
        return max(height)

def is_balance(root):
    if check_balance_tree(root) is not False:
        return True
    else:
        return False


def is_balance_2(root):
    return check_height(root) != 0


def check_height(root):
    if root is None:
        return 0
    left_height = check_height(root.left)
    right_height = check_height(root.right)
    h_diff = left_height - right_height
    if abs(h_diff) > 1:
        return False
    else:
        return max(left_height, right_height) + 1

