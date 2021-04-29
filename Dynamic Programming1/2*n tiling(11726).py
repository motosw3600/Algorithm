n = int(input())

n_rec = [0 for _ in range(n + 1)]

for i in range(n + 1):
    if i < 3:
        n_rec[i] = i
    else:
        n_rec[i] = n_rec[i -1] + n_rec[i - 2]

print(n_rec[n] % 10007)
