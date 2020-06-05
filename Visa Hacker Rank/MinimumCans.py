def minCans(total, used):
    total.sort(reverse=True)

    usedsum = sum(used)
    count = 0

    for i in range(len(total)):
        if total[i] <= usedsum:
            usedsum -= total[i]
            count += 1
        else:
            if usedsum == 0:
                break
            else:
                count += 1
                break
    return count

total = [3,3,3]
used = [2,2,3]
print( )

print(minCans(total, used))