N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

minus = 0
zero = 0
plus = 0

def cut(x, y, N):
    global minus
    global zero
    global plus

    check = paper[x][y]
    for i in range(N):
        for j in range(N):
            if check != paper[i+x][j+y]:
                leng = N//3
                cut(x, y, leng)
                cut(x, y+leng, leng)
                cut(x, y+2*leng, leng)
                cut(x+leng, y, leng)
                cut(x+leng, y+leng, leng)
                cut(x+leng, y+2*leng, leng)
                cut(x+2*leng, y, leng)
                cut(x+2*leng, y+leng, leng)
                cut(x+2*leng, y+2*leng, leng)
                return

    if check == 1:
        plus += 1
    elif check == 0:
        zero += 1
    elif check == -1:
        minus += 1


cut(0, 0, N)
print(minus)
print(zero)
print(plus)

