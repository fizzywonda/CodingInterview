from linkedlist.RemoveDups import *

"""
    Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e- >f 
"""

def delete_mid_node(xlist):
    p1 = xlist.head
    p2 = xlist.head
    prev = Node()

    while p1.next.next is not None:
        p1 = p1.next.next
        prev = p2
        p2 = p2.next
        if p1.next is None: break

    prev.next = p2.next

    return xlist.head

xlist = inputs()

if __name__ == '__main__':
    xlist.printlist()
    delete_mid_node(xlist)
    xlist.printlist()
