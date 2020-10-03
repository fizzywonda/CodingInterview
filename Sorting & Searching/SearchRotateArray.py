"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
lnput:find5in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
"""

def search(arr, x):
    start = 0
    end = len(arr) - 1
    return binary_search_helper(arr, x, start, end)


def binary_search_helper(array, x, start, end):
    if end >= start:
        mid = (start + end) // 2
        if array[mid] == x:
            return mid
        if array[mid] > x:
            if array[mid] > array[start] and array[start] <= x:
                return binary_search_helper(array, x, start, mid - 1)
            else:
                return binary_search_helper(array, x, mid+1, end)
        else:
            if array[mid] < array[end] and array[end] >= x:
                return binary_search_helper(array, x, mid + 1, end)
            else:
                return binary_search_helper(array, x, start, mid-1)
    return -1

if __name__ == '__main__':
    x = [10,50,20,0,5]  # [3,4,5,1,2]
    print(search(x,5))