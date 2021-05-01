A = int(input())

n_list = list(map(int, input().split()))
n_bum = [0 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if n_list[i] > n_list[j] and n_bum[i] < n_bum[j]:
            n_bum[i] = n_bum[j]
    n_bum[i] += 1

print(max(n_bum))
