A = int(input())

n_list = list(map(int, input().split()))
n_lnum = [0 for _ in range(A)]
for i in range(A):
    for j in range(i):
        if n_list[j] < n_list[i] and n_lnum[j] > n_lnum[i]:
            n_lnum[i] = n_lnum[j]
    n_lnum[i] += 1

m_val = max(n_lnum)
print(m_val)

s_list = []
for i in range(A - 1, -1, -1):
    if n_lnum[i] == m_val:
        s_list.append(n_list[i])
        m_val -= 1

s_list.reverse()
for i in s_list:
    print(i, end=' ')