import sys
N = int(input())

n_list = []
for i in range(N):
    p_list = list(map(int, sys.stdin.readline().split()))
    n_list.append(p_list)

n_list.sort(key=lambda x:(x[1], x[0]))
for list in n_list:
    print(list[0], list[1])
