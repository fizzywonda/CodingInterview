"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, {"at","" ,"" ,"", "ball", "","", "car", "","", "dad", "",""}
Output: 4
"""

def search(arr, x,):
    low = 0
    high = len(arr) -1
    return binary_search(arr, x, low, high)

def binary_search(arr, x, low, high):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        if arr[mid] == "":
            left = mid - 1
            right = mid + 1
            while True:
                if left < low and right > high:
                    return -1
                elif arr[left] != "":
                    mid = left
                    break
                elif arr[right] != "":
                    mid = right
                    break
                left -= 1
                right += 1
        if arr[mid] < x:
            return binary_search(arr, x, mid + 1, high)
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        else:
            return mid

if __name__ == '__main__':
    x = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(search(x, "car"))

