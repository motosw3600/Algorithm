N = int(input())

n_list = list(map(int, input().split()))
n_bic = [n_list[0]] + [0 for i in range(N - 1)]

for i in range(1, N):
    n_bic[i] = max(n_bic[i - 1] + n_list[i], n_list[i])

print(max(n_bic))