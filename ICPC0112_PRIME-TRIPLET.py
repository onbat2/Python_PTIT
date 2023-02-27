import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for i in range(2, n - 6):
        if(isPrime(i) and isPrime(i + 2) and isPrime(i + 6)):
            count += 1
        if(isPrime(i) and isPrime(i + 4) and isPrime(i + 6)):
            count += 1
    print(count)