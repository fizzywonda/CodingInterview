"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""

def sort_stack(stack):
    temp_stack = []
    while len(stack) > 0:
        element = stack.pop()
        if len(temp_stack) < 1:
            temp_stack.append(element)
        else:
            if element > temp_stack[len(temp_stack) - 1]:
                temp_stack.append(element)
            else:
                index = len(temp_stack) - 2
                while element < temp_stack[index]:
                    index -= 1
                temp_stack.insert(index + 1, element)

    while len(temp_stack) > 0:
        stack.append(temp_stack.pop())
    return stack


def sort_stack2(stack):  # another route
    temp_stack = []
    while len(stack) != 0:
        temp_element = stack.pop()
        while temp_element < peek(temp_stack):
            stack.append(temp_stack.pop())
        temp_stack.append(temp_element)
    while len(temp_stack) != 0:
        stack.append(temp_stack.pop())
    return stack


def peek(stack):
    if len(stack) == 0:
        return 0
    else:
        return stack[len(stack) - 1]


if __name__ == '__main__':
    stack = [3,2,4,5,1]
    sorted_stack = sort_stack2(stack)
    print(sorted_stack)

