def getPosition(val, arr, start, end):
    if start == end:
        return 0
    mid = (start + end)//2
    if arr[mid] >= val:
        if arr[mid-1] < val:
            return mid
        else:
            return getPosition(val, arr, mid + 1, end)
    elif arr[mid] <= val:
        if arr[mid+1] > val:
            return mid
        else:
            return getPosition(val, arr, start, mid - 1)


def getMinOp(pos, sortedarr):

    return(min(abs(0 - pos),abs(len(sortedarr) - pos)) *2 + 1)


def sorted_arangement(arr):
    totalOp = 0
    sortedarr = []
    for val in range(len(arr)):
        pos = getPosition(val, sortedarr, 0, len(sortedarr)-1)
        totalOp += getMinOp(pos, sortedarr)
        sortedarr.insert(pos, val)
    return totalOp



