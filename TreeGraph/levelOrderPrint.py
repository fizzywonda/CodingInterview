"""
Given a binary tree, print level order traversal in a way that nodes of all levels are printed in separate lines.
"""
from TreeGraph.MinimalTree import Node


def level_order(root):
    q = []
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            curr = q.pop()
            print(curr.data, end="")
            if curr.left_child:
                q.insert(0, curr.left_child)
            if curr.right_child:
                q.insert(0,curr.right_child)
            count -= 1
        print("\n")

if __name__ == '__main__':

    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    root.right_child.right_child = Node(6)

    print(level_order(root))