n = int(input())
m_lst = [int(x) for x in input().split()]
k = 0
while k < (len(m_lst) - 1):
    if (m_lst[k] + m_lst[k + 1]) % 2 == 0:
        m_lst.pop(k)
        m_lst.pop(k)
        k -= 2
    k += 1
    if k < 0: k = 0
print(len(m_lst))