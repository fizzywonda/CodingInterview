"""
Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.
"""
def palindromeSubStrs(s):
    pset = set()
    n = len(s)

    # table for storing results (2 rows for odd-
    # and even-length palindromes
    r = [[0 for i in range(n + 1)] for i in range(2)]

    # Find all sub-string palindromes from the given input
    # string insert 'guards' to iterate easily over s
    s = "@" + s + "#"

    for j in range(2):
        prad = 0  # length of 'palindrome radius'
        r[j][0] = 0

        i = 1
        while i <= n:

            # Attempt to expand palindrome centered at i
            while s[i - prad - 1] == s[i + j + prad]:
                prad += 1  # Incrementing the length of palindromic
                # radius as and when we find valid palindrome

            # Assigning the found palindromic length to odd/even
            # length array
            r[j][i] = prad
            k = 1
            while (r[j][i - k] != prad - k) and (k < prad):
                r[j][i + k] = min(r[j][i - k], prad - k)
                k += 1
            prad = max(prad - k, 0)
            i += k

            # remove guards
    s = s[1:len(s) - 1]

    # Put all obtained palindromes in a hash map to
    # find only distinct palindrome
    pset.add(s[0])
    for i in range(1, n):
        for j in range(2):
            for prad in range(r[j][i], 0, -1):
                pset.add(s[i - prad - 1: i - prad - 1 + 2 * prad + j])
        pset.add(s[i])

    return len(pset)
    # printing all distinct palindromes from hash map
    print ("Below are " + str(len(pset)) + " pali sub-strings")
    for i in pset:
        print(i)

    # Driver program


print(palindromeSubStrs("abaaa"))