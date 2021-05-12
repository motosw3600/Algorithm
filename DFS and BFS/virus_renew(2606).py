import sys

dic = {}

for i in range(int(sys.stdin.readline())):
    dic[i+1] = set()

for j in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

visited = []
def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

print(dic)
# dfs(1, dic)
bfs(1, dic)
print(visited)
print(len(visited) - 1)