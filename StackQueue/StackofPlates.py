"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.

"""

class Stackofplates:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def isfull(self, topstack):
        if len(topstack) == self.capacity:
            return True
        else:
            return False

    def is_empy(self, stack):
        if len(stack) == 0:
            return True
        else:
            return False

    def get_top_stack(self):
        if self.is_empy(self.stack):
            new_stack = []
            self.stack.append(new_stack)
            return self.get_top_stack()
        else:
            return self.stack[len(self.stack) - 1]

    def push(self, data):
        top_stack = self.get_top_stack()
        if not self.isfull(top_stack):
            top_stack.append(data)
        else:
            new_stack = [data]
            self.stack.append(new_stack)

    def pop(self):
        try:
            if len(self.stack) == 0:
                raise Exception("Stack is empty")
            else:
                top_stack = self.get_top_stack()
                if len(top_stack) == 1:
                    top_stack =  self.stack.pop()
                    top_element = top_stack.pop()
                    return top_element
                else:
                    top_element = top_stack.pop()
                    return top_element
        except Exception as e:
            raise e

    def pop_at(self, index):
        if index >= len(self.stack) or self.is_empy(self.stack):
            raise Exception("Out of bound")
        else:
            stack_at_index = self.stack[index]
            if len(stack_at_index) == 1:
                stack_at_index = self.stack.pop(index)
                top_element = stack_at_index.pop()
                return top_element
            else:
                top_element = stack_at_index.pop()
                return top_element



    def print_stack(self):
        print(self.stack)

if __name__ == '__main__':
    mystack = Stackofplates(2)
    for i in range(10):
        mystack.push(i)

    mystack.print_stack()

    print(mystack.pop())
    mystack.print_stack()

    print(mystack.pop())
    mystack.print_stack()

    print(mystack.pop())
    mystack.print_stack()

    mystack.push("a")
    mystack.print_stack()

    print(mystack.pop_at(2))
    mystack.print_stack()

    print(mystack.pop_at(2))
    mystack.print_stack()



