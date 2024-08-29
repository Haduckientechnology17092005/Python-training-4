import numpy as np
prime = []
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def prime_numbers_before(n):
    for i in range(2, n):
        if (isPrime(i)):
            prime.append(i)
    print(prime)

prime_numbers_before(100)