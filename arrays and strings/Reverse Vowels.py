"""
reverse only the vowels in a string
"""


def reverseVowels(s: str) -> str:
    vset = set(["a", "e", "i", "o", "u"])
    n = len(s)
    right = n - 1
    left = 0
    s = list(s)
    print(s)

    while left < right:
        if s[left] in vset and s[right] in vset:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        elif s[left] in vset:
            right -= 1

        elif s[right] in vset:
            left += 1

        else:
            left += 1
            right -= 1

    return "".join(s)

if __name__ == '__main__':
    print(reverseVowels("hello"))