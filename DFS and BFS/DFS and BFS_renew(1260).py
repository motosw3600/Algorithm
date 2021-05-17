import sys
input = sys.stdin.readline
n, M, start = map(int, input().split())
n_list = [[0] * (n + 1) for i in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(M):
    a, b = map(int, input().split())
    n_list[a][b] = 1
    n_list[b][a] = 1


def dfs(start):
    print(start, end=' ')
    visit[start] = 1 # 방문한걸 1으로 표시
    for i in range(1, n + 1):
        if visit[i] == 0 and n_list[start][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and n_list[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(start)
print()
bfs(start)