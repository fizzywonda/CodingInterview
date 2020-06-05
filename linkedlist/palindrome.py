from linkedlist.RemoveDups import *

"""
    Palindrome: Implement a function to check
    if a linked list is a palindrome.
"""

def palindrome(xlist):
    stack = []
    slow = xlist.head
    fast = xlist.head
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    """ check if the linkedlist is odd """
    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True

xlist = inputs()

if __name__ == '__main__':
    print(palindrome(xlist))
