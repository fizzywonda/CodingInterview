"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, data):
        self.stackA.append(data)

    def pop(self):
        if len(self.stackA) == 0:
            raise Exception
        while len(self.stackA) > 1:
            element = self.stackA.pop()
            self.stackB.append(element)
        first_element = self.stackA.pop()

        while len(self.stackB) > 0:
            return_element = self.stackB.pop()
            self.stackA.append(return_element)

        return first_element

if __name__ == '__main__':
    myqueue = MyQueue()
    for i in range(10):
        myqueue.push(i)

    for i in range(10):
        print(myqueue.pop())



