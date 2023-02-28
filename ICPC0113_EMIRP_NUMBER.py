import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    s = int(input())
    ans = []
    for i in range(10, s):
        if i != int(str(i)[::-1]) and isPrime(i) and isPrime(int(str(i)[::-1])):
            if int(str(i)[::-1]) < s and i not in ans and int(str(i)[::-1]) not in ans:
                ans.append(i)
                ans.append(int(str(i)[::-1]))
    for n in ans:
        print(n, end=" ")
    print()