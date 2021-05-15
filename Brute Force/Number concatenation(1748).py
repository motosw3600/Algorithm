n = int(input())
cnt = 0
n_len = len(str(n)) - 1
i = 0
while i < n_len:
    cnt += 9 * (10 ** i) * (i + 1)
    i += 1

cnt += (int(n) - (10 ** n_len) + 1) * (n_len + 1)
print(cnt)


