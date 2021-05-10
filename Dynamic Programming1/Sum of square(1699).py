N = int(input())

n_list = [0 for i in range(N + 1)]
square = [i * i for i in range(1, 317)]
# 1 4 9 16
for i in range(1, N + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(n_list[i - j])
    n_list[i] = min(s) + 1

print(n_list[N])
