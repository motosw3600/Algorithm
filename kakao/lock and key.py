import copy

def solution(key, lock):
    M = len(key)
    N = len(lock)
    extend_map = [[0 for _ in range(N*2+M)] for _ in range(N*2+M)]
    for x in range(N):
        for y in range(N):
            extend_map[x+M][y+M] = lock[x][y]

    keys = key
    for _ in range(4):
        keys = turn(keys)
        for x in range(0, M+N):
            for y in range(0, M+N):
                apply(x, y, M, keys, extend_map)

                if chain(extend_map, M, N):
                    return True

                deApply(x, y, M, keys, extend_map)

    return False

def apply(x, y, M, key, maps):
    for i in range(M):
        for j in range(M):
            maps[x+i][y+j] += key[i][j]

def deApply(x, y, M, key, maps):
    for i in range(M):
        for j in range(M):
            maps[x+i][y+j] -= key[i][j]

def chain(maps, M, N):
    for x in range(N):
        for y in range(N):
            if maps[M+x][M+y] != 1:
                return False
    return True

def turn(maps):
    turn_maps = copy.deepcopy(maps)
    leng = len(maps) - 1
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            turn_maps[x][y] = maps[leng - y][x]
    return turn_maps

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))