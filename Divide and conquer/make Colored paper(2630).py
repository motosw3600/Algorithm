n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))
white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    check = n_list[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != n_list[i][j]:
                cut(x, y, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return

    if check == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, n)
print(white)
print(blue)