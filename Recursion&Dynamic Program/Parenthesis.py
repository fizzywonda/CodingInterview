"""
Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: (( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
"""

def parens(number):
    index = 0
    result = set()
    return parenthesis(index, number, result)

def parenthesis(index, number, result):
    if index == number:
        return result

    result = insert(index, result)
    return parenthesis(index + 1, number, result)


def insert(index, result):
    if len(result) == 0:
        temp = set()
        temp.add("()")
        return temp

    temp_result = set()
    for valid_pairs in result:
        temp_result.add("()"+valid_pairs)
        for i in range(len(valid_pairs)):
            if valid_pairs[i] == "(":
                left = valid_pairs[:i+1]
                right = valid_pairs[i+1:]
                temp = left + "()" + right
                temp_result.add(temp)

    return temp_result

if __name__ == '__main__':
    par = parens(4)
    print(par)