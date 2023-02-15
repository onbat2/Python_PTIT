def minValue(s, x, y):
    return int(s.replace(y, x))
def maxValue(s, x, y):
    return int(s.replace(x, y))

t = int(input())
for i in range(t):
    x, y = [x for x in input().split()]
    if int(x) > int(y):
        x, y = y, x
    s1 = input().strip()
    if s1.count(' '):
        s1, s2 = s1.split()
    else:
        s2 = input()
    print(minValue(s1, x, y) + minValue(s2, x, y),
          maxValue(s1, x, y) + maxValue(s2, x, y))

