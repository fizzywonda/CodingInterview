"""
Magic Index: A magic index in an array A[ 1 .•. n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""

def magic_index(arr):
    return magic_index2(arr, 0, len(arr) - 1)


def magic_index2(arr, start, end):
    if end < start:
        return None
    mid = (start + end)/2
    if arr[mid] == mid:
        return mid
    if arr[mid] > mid:
        return magic_index2(arr, start, mid - 1)
    else:
        return magic_index2(arr, mid + 1, end)


"""
if the values are not distinct
"""

def magic_indexF(arr):
    return magic_indexF2(arr, 0, len(arr) - 1)


def magic_indexF2(arr, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    if arr[mid] == mid:
        return mid
    if arr[mid] > mid:
        left_index = min(arr[mid], mid)
        return magic_index2(arr, start, left_index)
    else:
        right_index = max(arr[mid], mid + 1)
        return magic_index2(arr, right_index, end)
