N, M, x, y, K = map(int, input().split(" "))

dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
maps = []
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for _ in range(N):
    maps.append(list(map(int, input().split(" "))))

cmds = list(map(int, input().split(" ")))

def rollDice(num):
    temp = dice.copy()
    if num == 1:
        dice[1] = temp[4]
        dice[4] = temp[6]
        dice[3] = temp[1]
        dice[6] = temp[3]
    elif num == 2:
        dice[1] = temp[3]
        dice[4] = temp[1]
        dice[3] = temp[6]
        dice[6] = temp[4]
    elif num == 4:
        dice[1] = temp[2]
        dice[2] = temp[6]
        dice[5] = temp[1]
        dice[6] = temp[5]
    elif num == 3:
        dice[1] = temp[5]
        dice[2] = temp[1]
        dice[5] = temp[6]
        dice[6] = temp[2]

for cmd in cmds:
    if 0 <= x + move[cmd-1][0] < N and 0 <= y + move[cmd-1][1] < M:
        rollDice(cmd)
        x += move[cmd-1][0]
        y += move[cmd-1][1]

        if maps[x][y] == 0:
            maps[x][y] = dice[6]
        else:
            dice[6] = maps[x][y]
            maps[x][y] = 0

        print(dice[1])

