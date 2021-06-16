from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(computers, i, visited)
            answer += 1

    return answer

def bfs(computers, com, visited):
    queue = deque([com])
    while queue:
        val = queue.popleft()
        visited[val] = True
        for i, value in enumerate(computers[val]):
            if val != i and value == 1 and visited[i] == False:
                queue.append(i)

