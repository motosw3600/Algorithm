import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    r_dis = r1 + r2
    R = [r1, r2, distance]
    m = max(R)
    R.remove(m)


    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance == r_dis or m == sum(R):
            print(1)
        elif m > sum(R):
            print(0)
        else:
            print(2)
