def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    return binary_search_helper(arr, x, start, end)

def binary_search_helper(array, x, start, end):
    if end >= start:
        mid = (start + end)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_helper(array, x, start, mid - 1)
        else:
            return binary_search_helper(array, x, mid+1, end)
    return -1

if __name__ == '__main__':
    x = [1,2,3,4,5]
    print(binary_search(x, 5))