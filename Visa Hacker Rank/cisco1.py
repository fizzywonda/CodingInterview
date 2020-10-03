def result(str):

    res = ""
    n = len(str)
    i = 0
    while i < n:
        curr = str[i]
        res =+ curr
        dup = 0
        while curr == str[i + 1]:
            dup +=2
            i =+ 1
        if dup != 0:
            res += str(dup)
            i =+ dup


if __name__ == '__main__':
    print(result("abaasass"))



