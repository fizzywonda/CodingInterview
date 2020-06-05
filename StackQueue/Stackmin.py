"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.min = 0

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, node):
        if self.isEmpty():
            node.min = node.data
            self.stack.append(node)
        else:
            topofstack = self.peek()
            if topofstack.min < node.data:
                node.min = topofstack.min
                self.stack.append(node)
            else:
                node.min = node.data
                self.stack.append(node)

    def pop(self):
        top_element = self.peek()
        self.stack.pop()
        return top_element

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def stackmin(self):
        top_element = self.stack[len(self.stack) - 1]
        return top_element.min

    def printstack(self):
         for i in self.stack:
             print(i.data, end="")

if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        node = Node(i)
        stack.push(node)

    stack.printstack()
    x = stack.stackmin()
    print(x)
