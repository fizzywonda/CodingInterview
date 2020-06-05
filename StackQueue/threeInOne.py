class Stack3:
    # array = []
    # numofstack = 0
    # sizeofelement = []

    def __init__(self, array, numofstack):
        self.array = array
        self.sizeofelement = []
        self.numofstack = numofstack
        for i in range(0, numofstack):
            self.sizeofelement.append(0)

    def isFull(self, stacknum):
        if stacknum != self.numofstack:
            stackcapacity = self.getstackcapacity(stacknum)
            stacklimitposition = (stackcapacity * (stacknum - 1)) + (stackcapacity - 1)
            return self.array[stacklimitposition] is not None
        else:
            stackcapacity = self.getstackcapacity(stacknum)
            temp = len(self.array) / self.numofstack
            stacklimitposition = (temp * (stacknum - 1) + (stackcapacity - 1))
            return self.array[stacklimitposition] is None

    def isEmpty(self, stacknum):
        if self.sizeofelement[stacknum - 1] == 0:
            return True
        else:
            return False

    def push(self,stackum, data):
        try:
            if self.isFull(stackum):
                raise ValueError("Stack is full")
            else:
                currstacksize = self.sizeofelement[stackum - 1]
                currstackcapacity = self.getstackcapacity(stackum)
                self.array[currstackcapacity * (stackum - 1) + currstacksize] = data
                self.sizeofelement[stackum - 1] += 1
        except ValueError as e:
            raise e
        finally:
            return


    def pop(self, stacknum):
        stackcapacity = self.getstackcapacity(stacknum)
        top_element = self.array[stackcapacity * (stacknum - 1)]
        self.array[stackcapacity * (stacknum - 1)] = None
        self.sizeofelement[stacknum - 1] -= 1
        return top_element

    def getstackcapacity(self, stacknum):
        if len(self.array) % self.numofstack != 0 and stacknum == self.numofstack: # stacksize for the last stack in an odd array
            stacksize = (len(self.array)//self.numofstack) + (len(self.array) % self.numofstack)
        else:
            stacksize = len(self.array)//self.numofstack

        return stacksize

    def printstack(self):
        print(self.array)


if __name__ == '__main__':
    arr = []
    for i in range(6):
        arr.append(None)
    print(arr)

    mystack = Stack3(arr, 3)

    mystack.push(1, 3)
    mystack.push(2, 9)
    mystack.push(1, 5)
    mystack.push(1, 5)





    mystack.printstack()

