"""""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
"""""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addDigit(final, sumdigit, carry):
    if sumdigit > 9:
        carry = sumdigit // 10
        sumdigit = sumdigit % 10
    else:
        carry = 0
    current = final
    while current.next is not None:
        current = current.next
    current.next = ListNode(sumdigit)
    return final, carry


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sumdigit = l1.val + l2.val
        if sumdigit > 9:
            carry = sumdigit // 10
            sumdigit = sumdigit % 10
            final = ListNode(sumdigit)
        else:
            final = ListNode(sumdigit)
        l1 = l1.next
        l2 = l2.next

        while l1 is not None or l2 is not None or carry != 0:

            if l1 is not None and l2 is not None:
                sumdigit = l1.val + l2.val + carry
                final, carry = addDigit(final, sumdigit, carry)
                l1 = l1.next
                l2 = l2.next

            elif l1 is not None and l2 is None:
                sumdigit = l1.val + carry
                final, carry = addDigit(final, sumdigit, carry)
                l1 = l1.next

            elif l1 == None and l2 is not None:
                sumdigit = l2.val + carry
                final, carry = addDigit(final, sumdigit, carry)
                l2 = l2.next

            else:
                sumdigit = carry
                final, carry = addDigit(final, sumdigit, carry)

        return final

