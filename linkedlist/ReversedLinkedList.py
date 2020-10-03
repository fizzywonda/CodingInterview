from linkedlist.RemoveDups import *


class LinkedList2(Linkedlist):
    def reverse(self, ):
        prev = None
        curr = self.head
        nxt = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev



def inputs():
    data = [1, 2, 3, 2, 4, 5, 1,4]  # ["a", "b", "c", "n", "a"]
    xlist = Linkedlist()
    xlist.head = Node(data[0])
    current = xlist.head
    for i in data[1:]:
        current.next = Node(i)
        current = current.next
    return xlist

if __name__ == '__main__':
    x = inputs()
    x.printlist()
    x.reverse()
    x.printlist()