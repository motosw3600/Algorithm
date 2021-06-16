from itertools import chain
def solution(n):
    res = [[None] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(n - i):
            if i % 3 == 0:
                x += 1

            elif i % 3 == 1:
                y += 1

            elif i % 3 == 2:
                x -= 1
                y -= 1

            res[x][y] = num
            num += 1

    return list(chain(*res))