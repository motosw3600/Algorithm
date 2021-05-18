N = int(input())

n_list = [[0] * N for i in range(N)]
visited = [[0] * N for i in range(N)]
cnt = 0
h_cnt = 0
c_list = []

for i in range(N):
    h_num = input()
    for val in range(len(h_num)):
        n_list[i][val] = int(h_num[val])

def find_list(x, y):

    r_list = []
    if x - 1 >= 0:
        r_list.append([x - 1, y])
    if x + 1 < N:
        r_list.append([x + 1, y])
    if y - 1 >= 0:
        r_list.append([x, y - 1])
    if y + 1 < N:
        r_list.append([x, y + 1])

    return r_list



def bfs(s_x, s_y):
    global cnt
    cnt += 1
    num = 1
    stack = [[s_x, s_y]]
    visited[s_x][s_y] = 1
    while stack:
        vlist = stack.pop(0)
        a = vlist[0]
        b = vlist[1]
        for flist in find_list(a, b):
            if n_list[flist[0]][flist[1]] == 1 and visited[flist[0]][flist[1]] == 0:
                stack.append([flist[0], flist[1]])
                visited[flist[0]][flist[1]] = 1
                num += 1

    return num


for i in range(N):
    for j in range(N):
        if n_list[i][j] == 1 and visited[i][j] == 0:
            hnum = bfs(i, j)
            c_list.append(hnum)

print(cnt)
for i in sorted(c_list):
    print(i)