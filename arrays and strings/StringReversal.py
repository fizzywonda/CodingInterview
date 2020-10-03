"""
reverse a string; all string
"""


def reverse(string):
    rev = ""
    for i in string:
        rev = i + rev
    return rev

"""
reverse each word
"""
def revword(string):
    splitword = string.split(" ")
    rev = splitword[0]
    for word in splitword[1:]:
        temp = ""
        for letter in word:
            temp = letter + temp
        rev = rev + " " + temp
    return rev


""" 
Reverse each word in a string (linear time)
"""


def revword2(string):
    temp = ""
    final = ""
    n = len(string)
    for i in range(n):
        if string[i] is not " ":
            temp = string[i] + temp
            if i == n-1:
                final += temp
        else:
            final += temp
            final += " "
            temp = ""

    return final


if __name__ == '__main__':
    x = "this am goes boy "
    print(reverse(x))
    print(revword2(x))