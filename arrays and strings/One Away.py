"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def oneAway(x,y):
    if len(x) == len(y):
        return checkSamelength(x,y)
    else:
        if abs(len(x) - len(y)) > 1:
            return False
        else:
            return checkDiffLength(x,y)


def hashit(x):
    dic = {}
    for i in range(len(x)):
        dic[x[i]] = i
    return dic


def checkSamelength(x,y):
    dic = hashit(x)

    count = 0
    for i in y:
        if i not in dic.keys():
            count += 1
        if count > 1:
            return False
    return True

def checkDiffLength(x,y):
    if len(x) > len(y):
        return smallInLarge(x,y)
    else:
        return smallInLarge(y,x)

def smallInLarge(x,y):
    dic = hashit(x)
    count = 0
    for i in y:
        if i not in dic.keys():
            count += 1
        if count > 0:
            return False

    return True

if __name__ == '__main__':


    x = "pale"
    y = "bae"
    print(oneAway(x,y))



