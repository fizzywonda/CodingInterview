"""
    Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
    node. Note that the intersection is defined based on reference, not value. That is, if the kth
    node of the first linked list is the exact same node (by reference) as the jth node of the second
    linked list, then they are intersecting.
"""

def intersection(xlist, ylist):

    xlen, xtail = check_length_and_tail(xlist)
    ylen, ytail = check_length_and_tail(ylist)

    if xtail == ytail:
        if xlen == ylen:
            return equallist(xlist, ylist)
        elif xlen > ylen:
            diff = xlen - ylen
            return unequallist(xlist, ylist, diff)
        else:
            diff = ylen - xlen
            return unequallist(ylist, xlist, diff)
    else:
        return False


def check_length_and_tail(xlist):
    curr = xlist.head
    lenght = 0

    while curr is not None:
        lenght += 1
    return lenght,curr


def equallist(xlist, ylist):
    xcurr = xlist.head
    ycurr = ylist.head
    while xcurr is not None:
        if xcurr == ycurr:
            return xcurr, True
        xcurr = xcurr.next


def unequallist(xlist, ylist, diff):
    xcurr = xlist.head
    ycurr = ylist.head
    for i in range(len(diff)):
        xcurr = xcurr.next

    while xcurr is not None:
        if xcurr == ycurr:
            return xcurr, True
        xcurr = xcurr.next
        ycurr = ycurr.next
