import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n_dic = {}
visited = [False] * N

for i in range(N):
    n_dic[i] = list()

for _ in range(M):
    a, b = map(int, input().split())
    n_dic[a].append(b)
    n_dic[b].append(a)

# dfs
def dfs(start, number):
    if number == 4:
        print(1)
        exit()
    for i in n_dic[start]:
        if visited[i] is False:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)

