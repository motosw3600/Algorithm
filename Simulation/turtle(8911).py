T = int(input())

moves = []
for _ in range(T):
    moves.append(input())

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for move in moves:
    way = 500
    wayPoint = [[0, 0]]
    x = 0
    y = 0
    for cmd in move:
        if cmd == "F":
            direct = direction[way % 4]
            x += direct[0]
            y += direct[1]
            wayPoint.append([x, y])
        elif cmd == "L":
            way -= 1
        elif cmd == "R":
            way += 1
        elif cmd == "B":
            direct = direction[way % 4]
            x -= direct[0]
            y -= direct[1]
            wayPoint.append([x, y])


    width = max(wayPoint, key=lambda x:x[0])[0] - min(wayPoint, key=lambda x:x[0])[0]
    height = max(wayPoint, key=lambda x:x[1])[1] - min(wayPoint, key=lambda x:x[1])[1]
    print(width * height)