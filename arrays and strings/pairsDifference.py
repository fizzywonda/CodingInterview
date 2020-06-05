"""

"""
def pairsDifference(arr,k):
    dic = {}
    count = 0
    for i in range(len(arr)):
        dic[i]= arr[i]
    for i in range(len(arr)):
        a = arr[i] - k
        b =arr[i] + k
        if a in dic.values():
            count += 1
        if b in dic.values():
            count += 1
        del dic[i]

    return count


if __name__ == '__main__':

    arr = [1,7,5,9,2,12,3]
    print(pairsDifference(arr,2))
