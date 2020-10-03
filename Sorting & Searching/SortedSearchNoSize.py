"""
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
"""


class Listy:
    def __init__(self, mylist):
        self.mylist = mylist

    def elementAt(self, index):
        if index > len(self.mylist) - 1:
            return -1
        else:
            return self.mylist[index]


def search(arr, value):
    index = 1
    while arr.elementAt(index) != -1 and arr.elementAt(index) < value:
        index *=2
    return binary_search(arr, value, index//2, index)


def binary_search(arr, value, low, high):
    if low <= high:
        midindex = (low + high)//2
        mid = arr.elementAt(midindex)
        if mid == -1 or mid > value:
            return binary_search(arr, value, low, midindex - 1)
        elif mid < value:
            return binary_search(arr, value, midindex + 1, high)
        else:
            return midindex

    return -1

if __name__ == '__main__':
    x = [1,2,3,4,5,6]
    mylist = Listy(x)
    print(search(mylist, 1))