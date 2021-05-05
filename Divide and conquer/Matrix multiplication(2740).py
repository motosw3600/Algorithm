N, M = map(int, input().split())
a_list = [list(map(int, input().split())) for x in range(N)]
O, K = map(int, input().split())
b_list = [list(map(int, input().split())) for x in range(O)]

def matrix_num(x, y):
    n = 0
    for i in range(M):
        n += (a_list[x][i] * b_list[i][y])
    return n

for i in range(N):
    for j in range(K):
        print(matrix_num(i, j), end=" ")
    print()

