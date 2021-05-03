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
print(n_lnum)

s_list = []
print(s_list)

for k in range(len(n_lnum)):
    if len(s_list) > 0:
        if n_lnum[k] 

# for k in range(1, m_val + 1):
#     for m in range(0, len(n_lnum)):
#         if k == n_lnum[m] and s_list[k - 1] < n_list[m]:
#             s_list.append(n_list[m])
#             break

