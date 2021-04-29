n = int(input())

n_list = [0, 1, 3]

for j in range(3, n + 1):
    n_list.append(n_list[j - 1] + n_list[j - 2] * 2)

print(n_list[n] % 10007)

