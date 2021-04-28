n = int(input())

n_rec = [0 for _ in range(n + 1)]

for i in range(n + 1):
    if i < 3:
        n_rec[i] = i
    else:
        for j in range(1, (i - 1) // 2 + 1):
            print(i, i - j)
            n_rec[i] += n_rec[i - j]
        if i % 2 == 0:
            n_rec[i] += 2


print(n_rec)
print(n_rec[n])
