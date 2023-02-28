import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def check(n):
    m_list = ['2', '3', '5', '7']
    sum = 0
    for i in n:
        if i not in m_list:
            return False
        sum += int(i)
        if isPrime(sum):
            return True
        return False

t = int(input())
for i in range(t):
    s = input()
    if isPrime(int(s)) and isPrime(int(str(s)[::-1])) and check(s):
        print('Yes')
    else:
        print('No')