"""
Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number x (the number of values less than or equal to x).
Implement the data structures and algorithms to support these operations. That is, implement
the method track(int x), which is called when each number is generated, and the method
getRankOfNumber(int x), which returns the number of values less than or equal to x (not
including x itself).
EXAMPLE
Stream(in order of appearance):5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(l) 0
getRankOfNumber(3) 1
getRankOfNumber(4) 3
"""

class BST:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None
        self.left_size = 0

    def insert(self, x):
        if x <= self.data:
            if self.leftnode is None:
                self.leftnode = BST(x)
            else:
                self.leftnode.insert(x)
            self.left_size += 1
        else:
            if self.rightnode is None:
                self.rightnode = BST(x)
            else:
                self.rightnode.insert(x)

def get_rank(tree, x):
    if tree.data == x:
        return tree.left_size
    elif x < tree.data:
        return get_rank(tree.leftnode, x)
    else:
        return tree.left_size + 1 + get_rank(tree.rightnode, x)


if __name__ == '__main__':
    x = [3,4,1,2,4,5]
    tree = BST(x[0])
    for i in range(1, len(x)):
        tree.insert(x[i])

    rank = get_rank(tree, 4)
    print(rank)