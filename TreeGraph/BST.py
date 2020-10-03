"""
Binary Search Tree implementation
"""

class BST:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None

    def insert(self, x):
        if x <= self.data:
            if self.leftnode is None:
                self.leftnode = BST(x)
            else:
                self.leftnode.insert(x)
        else:
            if self.rightnode is None:
                self.rightnode = BST(x)
            else:
                self.rightnode.insert(x)

# Inorder traversal to print the BST
def in_order(node):
    if node is not None:
        in_order(node.leftnode)
        print(node.data)
        in_order(node.rightnode)

if __name__ == '__main__':
    x = [3,4,1,2,5]
    tree = BST(x[0])
    for i in range(1, len(x)):
        tree.insert(x[i])

    in_order(tree)