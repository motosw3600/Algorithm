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

for combi in combination:
    arr = [[dis[c] for c in combi] for dis in distance]
    arr_sum = sum(list(map(lambda x:min(x), arr)))
    result = arr_sum if result > arr_sum else result

print(result)