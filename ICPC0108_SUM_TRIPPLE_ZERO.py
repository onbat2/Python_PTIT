t = int(input())

for i in range(t):
    n = int(input())
    m_list = sorted([int(x) for x in input().split()])
    dem = 0
    for i in range(0, n - 2):
        l = i + 1
        r = len(m_list) - 1
        x = m_list[i]
        while l < r:
            if (x + m_list[l] + m_list[r]) == 0:
                dem += 1
                l += 1
            elif (x + m_list[l] + m_list[r]) < 0:
                l += 1
            else:
                r -= 1
    print(dem)


