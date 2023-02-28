def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num

t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for c in s:
        sum += factorial(int(c))
    if sum == int(s):
        print('Yes')
    else:
        print('No')