"""
Create a sorted array from an unsorted array
"""

def create(arr):
    n = len(arr)
    b = []
    for i in range(n):
        if len(b) == 0:
            b.append(arr[i])
            continue

        start = 0
        end = len(b) - 1
        position = 0

        while start <= end:
            mid = (start + end) // 2
            if b[mid] == arr[i]:
                position = mid +1
                b.insert(max(0, position), arr[i])
                break

            # if mi
            if b[mid] < arr[i]:
                start = mid+1
            else:
                end = mid - 1

            if start > end:
                position = start
                b.insert(max(0, position), arr[i])
                break

    return b

if __name__ == '__main__':
    arr = [2,5,4,9,8,2]
    print(create(arr))