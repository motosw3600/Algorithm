from collections import deque
move = [[1,0], [-1, 0], [0, 1], [0, -1]]
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    flag = [[-1 for i in range(n)] for j in range(m)]
    q = deque()
    flag[0][0] = 1
    q.append([0, 0])

    while q:
        val = q.popleft()
        x = val[0]
        y = val[1]
        for mov in move:
            nx = x + mov[0]
            ny = y + mov[1]
            if -1 < nx < n and -1 < ny < m:
                if maps[ny][nx] == 1 and flag[ny][nx] == -1:
                    flag[ny][nx] = flag[y][x] + 1
                    q.append([nx, ny])

    print(flag[-1][-1])

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])