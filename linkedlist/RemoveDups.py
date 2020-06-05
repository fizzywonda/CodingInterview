""""
        R􀂧mov􀂧 Dups! Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
"""
class Node:

    # def __int__(self):
    #     self.data = None
    #     self.next = None

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self,):
        self.head = Node()

    def removedup(self):
        hashset = set()
        current = self.head
        previous = Node()
        while current is not None:
            if current.data in hashset:
                previous.next = current.next
            else:
                hashset.add(current.data)
                previous = current
            current = current.next

    def find(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return current
            current = current.next
        return False

    def fillup(self, x):
        self.head.data = x[0]
        current = self.head
        for i in x[1:]:
            current.next = Node(i)
            current = current.next

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.data, "->", end='')
            current = current.next
        print()

def inputs():
    data = [1, 2, 3, 2, 4, 5, 1,4]  # ["a", "b", "c", "n", "a"]
    xlist = Linkedlist()
    xlist.head = Node(data[0])
    current = xlist.head
    for i in data[1:]:
        current.next = Node(i)
        current = current.next
    return xlist

# x = [1, 2, 3, 2, 4, 5, 1,4]
# l = Linkedlist()
# l.fillup(x)
# l.printlist()

if __name__ == '__main__':
    xlist = inputs()

    xlist.printlist()
    xlist.removedup()
    xlist.printlist()





