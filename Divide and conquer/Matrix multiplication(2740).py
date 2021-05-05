N, M = map(int, input().split())
a_list = []
b_list = []
for _ in range(N):
    a_list.append(list(map(int, input().split())))

O, K = map(int, input().split())
for _ in range(O):
    b_list.append(list(map(int, input().split())))

c_list = [[0 for x in range(N)] for y in range(K)]

def matrix_num(a, b):
    n = 0
    for i in range(M):
        for j in range(O):
            n += (a_list[i][j] + b_list[j][i])
    return n

for i in range(K):
    for j in range(N):
        c_list[i][j] = 

a_list[0][0], a_list[0][1], b_list[0][0], b_list[1][0]
a_list[0][0], a_list[0][1], b_list[1][0], b_list[1][1]
a_list[0][0], a_list[0][1], b_list[2][0], b_list[1][2]