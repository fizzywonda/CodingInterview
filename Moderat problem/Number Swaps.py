"""
Number Swapper: Write a function to swap a number in place (that is, without temporary variables).
"""

def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(x,y)

if __name__ == '__main__':
    x = 2
    y = 3

    swap(x, y)
    # print(x,y)