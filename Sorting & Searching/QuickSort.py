def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr,low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if left < right:
            swap(arr,left,right)
        else:
            done = True
    swap(arr, low, right)
    return right

def quicksorthelp(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksorthelp(arr, low, pivot-1)
        quicksorthelp(arr, pivot + 1, high)


def quicksort(arr):
    low = 0
    high = len(arr) - 1
    quicksorthelp(arr, low, high)
    return arr

if __name__ == '__main__':
    x = [6,8,9,2,3,1,7,5,0,4,5,6]
    print(quicksort(x))
