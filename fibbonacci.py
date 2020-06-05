def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n -1) + fib(n-2)

def fibiterate(n):
    if n <= 1:
        return n
    prev,prevprev = 0, 0
    curr = 1

    for i in range(1,n):
        prevprev = prev
        prev = curr
        curr = prev + prevprev
    return curr



print(fibiterate(7))