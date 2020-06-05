def variantCounts(n, s0, k, b, m, a):
    sideLst = [s0]
    count = 0
    for i in range(1, n):
        side = ((k*sideLst[i-1] + b) % m) + 1 + sideLst[i-1]
        sideLst.append(side)
    for i in range(len(sideLst)):
        for j in range(i, len(sideLst)):
            if sideLst[i] * sideLst[j] <= a:
                if sideLst[i] == sideLst[j]:
                    count += 1
                else:
                    count += 2
    return count





print(variantCounts(3, 1,1,1,2,4))