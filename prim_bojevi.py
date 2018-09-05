"""
printa zadan broj prim brojeva
"""

from math import sqrt
n = int(input("enter number of prime numbers you want to print out?\n"))
def isPrime(n):
    if n == 2:
        return True
    elif n < 1 or not n % 2:
        return False
    for i in range(3, int(sqrt(n)+1), 2):
        if not n % i:
            return False
    else:
        return True

def primesList(num):
    primes = [2,]
    noPrimes = 1
    testNum = 3
    
    while noPrimes < num:
        if isPrime(testNum):
            primes.append(testNum)
            noPrimes += 1
        testNum += 1
    return primes

for i in primesList(n):
    print(primesList(n).index(i)+1,"-", i)