"""
Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods
"""
import random


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.sub_tree_size = 0

    def get_random_node(self):
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.sub_tree_size
        index = random.randrange(self.sub_tree_size)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert(self, data):

        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

        self.sub_tree_size += 1

    def find(self, data):
        if self.data == data:
            return self
        elif data < self.data:
            if self.left is None:
                return None
            else:
                return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return None
            else:
                return self.right.find(data)
        else:
            return None


if __name__ == '__main__':
    a = TreeNode(4)
    a.insert(2)
    a.insert(5)
    a.insert(1)
    a.insert(3)
    a.insert(6)


    print(a.get_random_node().data)