def longestSubseq(arr):
    num_of_subseq = []
    for i in range(len(arr)):
        num_of_subseq.append(1)

    for j in range(1, len(arr)):
        for i in range(0, j):
            if ((arr[i] < arr[j]) and (num_of_subseq[i] <= num_of_subseq[j])):
                num_of_subseq[j] = num_of_subseq[i] + 1

    return max(num_of_subseq)

x = [3,4,-1,0,6,2,3]
# print(x)
print(longestSubseq(x))