"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""


class Tower:
    def __init__(self, Id):
        self.stack = []
        self.Id = Id

    def add_disk(self, disk):
        if len(self.stack) != 0 and self.stack[len(self.stack) - 1] < disk:
            print("error")
        self.stack.append(disk)

    def pop(self):
        return self.stack.pop()

    def print_stack(self):
        print("Stack " + self.Id)
        for i in self.stack:
            print(i)

    def tower_of_hanoi(self, n, destination, buffer):
        if n == 0:
            return
        self.tower_of_hanoi(n-1, buffer, destination)
        self.move_top(destination)
        buffer.tower_of_hanoi(n-1, destination, self)


    def move_top(self, destination):
        disk = self.pop()
        destination.add_disk(disk)

if __name__ == '__main__':
    n = 3
    a = Tower("a")
    b = Tower("b")
    c = Tower("c")

    for i in range(n, 0, -1):
        a.add_disk(i)
    a.print_stack()
    a.tower_of_hanoi(n, b, c)
    print("after moving")
    a.print_stack()
    b.print_stack()