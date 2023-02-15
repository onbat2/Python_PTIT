t = int(input())
for i in range(t):
    n, d = [int(x) for x in input().split()]
    m_list = [int(x) for x in input().split()]
    for i in range(d, n):
        print(m_list[i], end = " ")
    for i in range(0, d):
        print(m_list[i], end = " ")
    print()