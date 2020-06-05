"""
    Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
    beginning of the loop.
    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
    as to make a loop in the linked list.
    EXAMPLE
    Input:A - > B - > C - > D - > E - > C [the same C as earlier]

    Output:C

"""

from linkedlist.RemoveDups import *

def loopdetect(xlist):
    h = set()

    curr = xlist
    count = 0
    while curr is not None and count <=10:
        if curr in h:
            return curr.data
        else:
            h.add(curr)
        curr = curr.next
        count += 1

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c



def printNodelist(node):
    curr = node
    count = 0
    while count < 10:
        print(curr.data)
        curr = curr.next
        count += 1

# printNodelist(a)

print(loopdetect(a))