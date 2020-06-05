"""
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine ifT2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""

""" 
Approach 1: do a preoder traversal of TI and T2 putting "x" in place of null node to make the tree unique
regardless of  its structure
then check traversed T2 in T1
"""
def check_subtree(root_a, root_b):
    trav_a = inorder(root_a)
    trav_b = inorder(root_b)

    if trav_b in trav_a:
        return True
    else:
        return False


def inorder(root_node, string):  # in_order traversal using "x" in place of null nodes
    if root_node is None:
        return string + "x"
    string = string + root_node.data
    inorder(root_node.left, string)
    inorder(root_node.right, string)
    return string


""" Approach2: locate the root of T2 in T1,
 then match the subtree of the found node with T2
 """

def check_subtree2(root_a, root_b):
    if root_a == None:
        return False
    if root_a.data == root_b.data and match(root_a, root_b):
        return True
    return check_subtree2(root_a.left, root_b) or check_subtree2(root_a.right, root_b)

def match(root_a, root_b):
    if root_a is None and root_b is None:
        return True
    if root_a.data == root_b.data:
        return match(root_a.left, root_b.left) and match(root_a.right, root_b. right)
    return False

