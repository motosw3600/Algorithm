n = int(input())

n_list = [[0,1], [1,0]]

for i in range(2, n):
    n_list.append([sum(n_list[i - 1]), n_list[i - 1][0]])

print(sum(n_list[n - 1]))
