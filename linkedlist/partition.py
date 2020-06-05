""""
        Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input:
    Output:
    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from linkedlist.RemoveDups import *

def partition(xlist, k):
    less = Linkedlist()

    greater = Linkedlist()
    current = xlist.head
    while current is not None:
        nextnode = current.next
        if current.data < k:
            if less.head.data is None:
                current.next = None
                less.head = current
            else:
                current.next = less.head
                less.head = current
        else:
            if greater.head.data is None:
                current.next = None
                greater.head = current
            else:
                current.next = greater.head
                greater.head = current
        current = nextnode

    curr_less = less.head

    while curr_less.next is not None:
        curr_less = curr_less.next

    curr_less.next = greater.head

    return less


if __name__ == '__main__':
    xlist = inputs()
    xlist.printlist()
    final = partition(xlist, 3)
    final.printlist()