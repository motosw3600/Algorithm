# 체스판 다시 칠하기 문제
# brute Force로 범위를 탐색하면서 구현
# 총 2가지 케이스를 한번에 탐색하면서 구현
N, M = map(int, input().split())
n_list = []

for _ in range(N):
    n_list.append(input())

val_list = []

for x in range(N - 7):
    for y in range(M - 7):
            first_W = 0
            first_B = 0
            num = 0
            for i in range(x, x + 8):
                for j in range(y, y + 8):
                    if (i + j) % 2 == 0:
                        if n_list[i][j] != 'W':
                            first_W = first_W + 1
                        if n_list[i][j] != 'B':
                            first_B = first_B + 1
                    else:
                        if n_list[i][j] != 'B':
                            first_W = first_W + 1
                        if n_list[i][j] != 'W':
                            first_B = first_B + 1
            val_list.append(first_W)
            val_list.append(first_B)


print(min(val_list))
