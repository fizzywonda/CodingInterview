"""
Normal Merging of two sorted array
"""
def merge(arr1,arr2):
    i, j, k = 0, 0, 0
    merged =[None for i in range(len(arr1) + len(arr2))]

    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            merged[k] = arr1[i]
            i += 1
            k += 1
        else:
            merged[k] = arr2[j]
            j += 1
            k += 1
    # if i < len(arr1):
    for x in range(i, len(arr1)):
        merged[k] = (arr1[x])
        k += 1
    # if j < len(arr2):
    for y in range(j, len(arr2)):
        merged[k] = (arr2[y])
        k += 1
    return merged

"""
merge for mergesort: merging two sorted part of an array
"""

def merge2(arr, low, mid, high):
    helper = [arr[i] for i in range(len(arr))]

    lowright = mid + 1
    current = low

    while low <= mid and lowright <= high:
        if helper[low] < helper[lowright]:
            arr[current] = helper[low]
            current += 1
            low += 1
        else:
            arr[current] = helper[lowright]
            lowright += 1
            current += 1
    remain = mid - low

    # for i in range(remain+1):
    #     arr[current + i] = helper[low + i]


    for i in range(low, mid+1):
        arr[current] = helper[i]
        current += 1

    # if lowright < high:
    #     for i in range(lowright, high + 1):
    #         arr[current+i] = merged[i]
    #         current += 1

def mergesort(arr):
    low = 0
    high = len(arr) - 1

    mergesorthelp(arr, low, high)
    return arr


def mergesorthelp(arr,low,high):
    if low < high:
        mid = (low + high)//2
        mergesorthelp(arr, low, mid)
        mergesorthelp(arr, mid+1, high)
        merge2(arr, low, mid, high)


if __name__ == '__main__':
    x = [5,3,1,9,2,7,8]
    y,q = [2,5,8,9,10], [1,3,7]
    # print(merge(y,q))
    print (mergesort(x))
