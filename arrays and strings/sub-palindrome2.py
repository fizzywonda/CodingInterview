def palindrome():
    def ispalindrome(string):
        return string == string[::-1]
    s = input()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub_str = s[i:j]
            if ispalindrome(sub_str):
                palindromes.add(sub_str)
    return (len(palindromes))

print(palindrome())