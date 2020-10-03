"""
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
"""

def peakValley(arr):
    arr.sort()
    i = 1
    while i < len(arr):
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i += 2
    return arr

def peakValley2(arr):
    i = 1
    while i < len(arr):
        if arr[i] > arr[i-1] and arr[i] > arr[i +1]:
            pass
        else:
            maxindex = checklargest(arr, i -1, i, i + 1)
            arr[i], arr[maxindex] = arr[maxindex], arr[i]
        i += 2


""" without sorting """
def checklargest(arr, a, b, c):
    aval = arr[a]
    bval = arr[b]
    cval = arr[c]
    maxindex = max(aval, bval, cval)
    if maxindex == aval:
        return a
    elif maxindex == bval:
        return b
    else: return c

if __name__ == '__main__':
    arr = [5, 3, 1, 2, 3]
    peakValley2(arr)
    print(arr)
