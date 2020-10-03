"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""
def sortedmerge(a, b, lastA, lastB):
    i = lastA - 1
    j = lastB - 1
    indexMerged = lastA + lastB - 1
    while j >= 0:
        if a[i] > a[j]:
            a[indexMerged] = a[i]
            i -= 1
        else:
            a[indexMerged] = b[j]
            j -= 1
        indexMerged -= 1


if __name__ == '__main__':
    a = [1, 3, 5, None, None, None, None]
    b = [2,4,6]
    sortedmerge(a,b, 3,3,)
    print(a)

