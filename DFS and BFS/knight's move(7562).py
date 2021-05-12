N = int(input())

for _ in range(N):
    chess = int(input())
    k_point = list(map(int, input().split()))
    m_point = list(map(int, input().split()))


stack = []
def dfs(start, dic):
    for i in dic[start]:
        if i not in stack:
            stack.append(i)
            dfs(i, list)

visited = []
def bfs(start, dic):
    queue = [start]
    while queue:
        val = queue.pop()
        for i in dic[val]:
            if i not in visited:
                queue.append(i)
                visited.append(i)