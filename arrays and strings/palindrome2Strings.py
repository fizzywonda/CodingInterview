""""
check if two strings are anagram of each other, ignore case, and punctuation
e.g. 'A dirty room -> dormitory
"""

import collections

def ispalindrome(s1, s2):
    s1 = [e.lower() for e in s1 if e.isalnum()]
    s2 = [e.lower() for e in s2 if e.isalnum()]

    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2


def ispalindrome2(s1, s2):
    s1 = [e.lower() for e in s1 if e.isalnum()]
    s2 = [e.lower() for e in s2 if e.isalnum()]

    if len(s1) != len(s2):
        return False

    s1count = collections.Counter(s1)

    for i in s2:
        if i in s1count:
            s1count[i] -= 1
            if s1count[i] < 1:
                del s1count[i]
        else:
            return False
    return True

if __name__ == '__main__':
    s1 = "dirty room"
    s2 = "dormitory "

    print(ispalindrome2(s1,s2))