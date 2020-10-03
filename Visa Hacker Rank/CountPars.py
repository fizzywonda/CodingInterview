def countpairs(arr, k):
    # pairset = {}
    # res = 0
    # j=0
    # n = len(numbers)
    # while j < n -1:
    #     i = j
    #     while i < n -1:
    #         if numbers[i] + k == numbers[i + 1]:
    #             if numbers[i] in pairset and numbers[i + 1] in pairset:
    #                 if pairset[numbers[i]] <= 1:
    #                     if pairset[numbers[i + 1]] <= 1:
    #                         if numbers[i] == numbers[i + 1]:
    #                             pairset[numbers[i]] += 2
    #                         else:
    #                             pairset[numbers[i]] += 2
    #                             pairset[numbers[i + 1]] = 1
    #                         res += 1
    #             elif numbers[i] in pairset and numbers[i + 1] not in pairset:
    #                 if pairset[numbers[i]] <= 1:
    #                     pairset[numbers[i]] += 1
    #                     pairset[numbers[i+1]] = 1
    #                     res += 1
    #                 else:
    #                     continue
    #
    #             elif numbers[i] not in pairset and numbers[i + 1] in pairset:
    #                 if pairset[numbers[i+1]] <= 1:
    #                     pairset[numbers[i]] = 1
    #                     pairset[numbers[i+1]] += 1
    #                     res += 1
    #                 else:
    #                     continue
    #             else:
    #                 pairset[numbers[i]] = 1
    #                 if numbers[i] == numbers[i + 1]:
    #                     pairset[numbers[i]] += 1
    #                 else:
    #                     pairset[numbers[i + 1]] = 1
    #                 res += 1
    #         i += 1
    #     j += 1
    count = 0
    arr.sort()
    l = 0
    r = 0
    n = len(arr)

    while r < n:
        if arr[r] - k == arr[l]:
            count += 1
            l += 1
            r += 1

        # arr[r] - arr[l] < sum
        elif arr[r] - k > arr[l]:
            l += 1
        else:
            r += 1
    return count
    # return res

if __name__ == '__main__':
    # num = [1,1,2,2,3,3]
    # num = [1,1,1,2]
    num = [1, 5, 3, 4, 2]
    k = 1
    print(countpairs(num, k))
