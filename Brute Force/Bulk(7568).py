N = int(input())

n_list = []
for i in range(N):
    n_list.append(list(map(int, input().split())))

for j in n_list:
    rank = 1
    for k in n_list:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end = ' ')

