def fib(n):
    if n <= 1:
        return n
    return fib(n -1) + fib(n -2)

"""
fibonacci Dynamic Programming
"""


def fib2(n):
    memo = [None for i in range(n + 1)]
    return fib_dynamic(n, memo)


def fib_dynamic(n,arr):
    if n <= 1:
        return n
    if arr[n] is None:
        arr[n] = fib_dynamic(n -1, arr) + fib_dynamic(n -2, arr)
    return arr[n]


print(fib2(5))