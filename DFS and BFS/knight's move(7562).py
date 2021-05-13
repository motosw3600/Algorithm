from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

k_xlist = [2, 2, 1, 1, -2, -2, -1, -1]
k_ylist = [1, -1, 2, -2, 1, -1, 2, -2]

def bfs(s_x, s_y, m_x, m_y):
    queue = deque()
    queue.append([s_x, s_y])
    n_list[s_x][s_y] = 1
    while queue:
        x, y = queue.popleft()
        if x == m_x and y == m_y:
            print(n_list[x][y] - 1)
            break
        for i in range(8):
            cx = x + k_xlist[i]
            cy = y + k_ylist[i]
            if 0 <= cx < c_size and 0 <= cy < c_size and n_list[cx][cy] == 0:
                queue.append([cx, cy])
                n_list[cx][cy] = n_list[x][y] + 1

for _ in range(N):
    c_size = int(input())
    k_x, k_y = map(int, input().split())
    m_x, m_y = map(int, input().split())
    n_list = [[0] * c_size for _ in range(c_size)]
    bfs(k_x, k_y, m_x, m_y)