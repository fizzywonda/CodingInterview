"""
clone a linkedlist with a next pointer and also an arbitrary node pointer
"""

def clone(node):
    Tclone = {}
    curr = node
    head_clone = None
    # creat a copy of each element mapped to his clone
    while curr.next:
        Tclone[curr] = curr
        curr = curr.next

    # iterate through the clone and connect the next and arb pointer
    for i in Tclone.keys():
        Tclone[i].next = Tclone[i.next]
        Tclone[i].abtr = Tclone[i.abtr]
        if head_clone is None:
            head_clone = Tclone[i]

    return head_clone