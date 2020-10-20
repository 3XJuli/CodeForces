n, m, a = map(int, input().split())
area = n * m
square = a * a
overf_n, overf_m = False, False
n_num = n // a

if n // a < n / a:
    n_num += 1
    overf_n = True

m_num = m // a
if m // a < m / a:
    m_num += 1
    overf_m = True
print(m_num * n_num)
