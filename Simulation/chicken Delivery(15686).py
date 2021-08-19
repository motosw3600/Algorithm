from itertools import combinations

N, M = map(int, input().split())

house = []
chicken = []
distance = []
result = 1000000

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

for h in house:
    dis = []
    for c in chicken:
        dis.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
    distance.append(dis)

cNum = [i for i in range(len(chicken))]
combination = list(combinations(cNum, M))

print(distance)
print(combination)

for data in distance:
    print(list(map(data, filter(lambda x:x.index == 0))))