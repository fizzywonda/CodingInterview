def longest_string(s):
    myset = {}
    longest = 0
    curr = []
    for i in s:
        if i in myset:
            index = myset[i]
            for j in range(index + 1):
                del myset[curr[j]]
            curr = curr[index + 1:]
            curr.append(i)
            myset[i] = len(curr) - 1

        else:
            curr.append(i)
            myset[i] = len(curr) - 1
            if len(curr) > longest:
                longest = len(curr)
    return longest


def jumpingOnClouds(c):
    minjump = 0
    i = 0
    while i < len(c) - 3:
        # print(c[i])
        # if i == len(c) - 2:
        #     minjump += 1
        #     i += 1
        if c[i + 2] == "0":
            minjump += 1
            i += 2
        else:
            # c[i + 1] == "0"
            minjump += 1
            i += 1
        # elif c[i + 1] == "0" and c[i + 2] == "1":
        #     minjump += 1
        #     i += 1
    return minjump + 1


# print(longest_string("asljlj"))
c="0010010"
print(jumpingOnClouds(c))