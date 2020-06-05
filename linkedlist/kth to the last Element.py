"""
    Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linkedlist.RemoveDups import *

class Linklist2(Linkedlist):

    def kth_to_last_element(self, k):
        P1 = self.head
        P2 = self.head

        for i in range(k):
            P1 = P1.next

        while P1 is not None:
            P1 = P1.next
            P2 = P2.next

        return P2

def inputs():
    data = [1, 2, 3, 2, 4, 5, 1, 4]
    xlist = Linklist2()
    xlist.head = Node(data[0])
    current = xlist.head
    for i in data[1:]:
        current.next = Node(i)
        current = current.next
    return xlist

if __name__ == '__main__':
    xlist = inputs()
    k = xlist.kth_to_last_element(3)
    print(k.data)