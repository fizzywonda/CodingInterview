"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
"""
"""Brute force Approach"""
def multiply(x, y):
    if y == 0:
        return 0
    result = x + multiply(x, y - 1)
    return result


"""improved approach"""
def multiply2(x, y):
    # get the bigger number
    small = x if x < y else y
    big = y if y > x else x

    return multiply_helper(small, big)


def multiply_helper(small, big):
    if small == 0:
        return 0
    if small == 1:
        return big

    # divide small by 2
    s = small >> 1
    side1 = multiply2(s, big)
    side2 = side1
    if small % 2 == 1:
        side2 = (side1 << 1) + big
        return side1 + side2
    return side1 + side2


""" optimized Approach (memoized)"""

def multiply3(x, y):
    small = x if x < y else y
    big = y if y > x else x
    memo = [None for i in range(small + 1)]

    return multiply_helper2(small, big, memo)


def multiply_helper2(small, big, memo):
    if small == 0:
        return 0
    if small == 1:
        return big

    if memo[small] is not None:
        return memo[small]

    s = small >> 1
    side1 = multiply3(s, big)
    side2 = side1

    if small % 2 == 1:
        side2 = (side1 << 1) + big
        memo[small] = side1 + side2

    memo[small] = side1 + side2
    return memo[small]





if __name__ == '__main__':
    x = 2
    y = 3
    result = multiply3(x, y)
    print(result)
