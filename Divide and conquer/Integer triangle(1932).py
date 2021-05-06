import sys
N = int(input())
t_list = []
for _ in range(N):
    t_list.append(list(map(int, sys.stdin.readline().split())))

c_list = [[t_list[0][0]]] + [[0] * i for i in range(2, N + 1)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            c_list[i][j] = c_list[i-1][0] + t_list[i][0]
        elif j == i:
            c_list[i][j] = c_list[i - 1][j - 1] + t_list[i][j]
        else:
            c_list[i][j] = max(c_list[i-1][j - 1], c_list[i - 1][j]) + t_list[i][j]

print(max(c_list[N - 1]))

