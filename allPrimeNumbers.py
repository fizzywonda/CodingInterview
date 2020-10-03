"""
Print out all prime numbers in a given number
"""

def allPrime(n):
    if n == 2:
        print(2)
    for i in range(2, n+1):
        if isPrime(i):
            print(i)

def isPrime(n):
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':

 print(allPrime(20))