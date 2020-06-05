"""
converts binary linkedlist into decimal
@:return decimal equivalence
"""
from linkedlist.RemoveDups import *


def getnumber(binary):
    length = -1
    runner = binary.head
    while runner is not None:
        length += 1
        runner = runner.next

    decimal = 0
    current = binary.head
    while length > -1:
        decimal += current.data * pow(2,length)
        current = current.next
        length -= 1

    return decimal

if __name__ == '__main__':
    binary = [0,1,0,1]
    l = Linkedlist()
    l.fillup(binary)
    # l.printlist()
    print(getnumber(l))
