import sys
from collections import deque
input = sys.stdin.readline
N, M, start = map(int, input().split())

n_dic = {}
for i in range(1, N+1):
    n_dic[i] = list()

for _ in range(M):
    a, b = map(int, input().split())
    n_dic[a].append(b)
    n_dic[b].append(a)

def dfs(start):
    d_values.append(start)
    for i in sorted(n_dic[start]):
        if i not in d_values:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    b_values.append(start)
    while queue:
        val = queue.popleft()
        for i in sorted(n_dic[val]):
            if i not in b_values:
                b_values.append(i)
                queue.append(i)


b_values = []
d_values = []
dfs(start)
bfs(start)
print(" ".join(map(str, d_values)))
print(" ".join(map(str, b_values)))