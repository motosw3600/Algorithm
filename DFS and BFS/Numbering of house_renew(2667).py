N = int(input())

n_list = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
apt = []

def dfs(x, y):
    global cnt
    cnt += 1
    n_list[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if n_list[nx][ny] == '1':
            dfs(nx, ny)

def bfs(x, y):
    global cnt
    cnt += 1
    stack = [(x, y)]
    n_list[x][y] = '0'
    while stack:
        val = stack.pop()
        a = val[0]
        b = val[1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if n_list[nx][ny] == '1':
                stack.append((nx, ny))
                n_list[nx][ny] = '0'
                cnt += 1

for i in range(N):
    for j in range(N):
        if n_list[i][j] == '1':
            cnt = 0
            bfs(i, j)
            apt.append(cnt)

print(len(apt))
for i in sorted(apt):
    print(i)