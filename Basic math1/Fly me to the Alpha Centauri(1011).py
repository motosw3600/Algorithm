T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dis = y - x - 1
    n = 1
    while dis > 0:
        dis -= n
        n += 1

    print(n)