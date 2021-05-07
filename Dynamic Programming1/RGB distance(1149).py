import sys
N = int(input())
h_list = []

for _ in range(N):
    h_list.append(list(map(int, sys.stdin.readline().split())))

b_list = [h_list[0]] + [[0] * 3 for i in range(N - 1)]

for i in range(1, N):
    b_list[i][0] = min(b_list[i - 1][1], b_list[i - 1][2]) + h_list[i][0]
    b_list[i][1] = min(b_list[i - 1][0], b_list[i - 1][2]) + h_list[i][1]
    b_list[i][2] = min(b_list[i - 1][0], b_list[i - 1][1]) + h_list[i][2]

print(min(b_list[N-1]))
