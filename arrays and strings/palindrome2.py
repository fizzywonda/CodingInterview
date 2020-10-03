""""
check if a string is a palindrome
"""

def palindrome(s):
    left = 0
    right = len(s)- 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def palindrome2(s):
    return s == s[::-1]

if __name__ == '__main__':
    x = "madam"

    print(palindrome2(x))
