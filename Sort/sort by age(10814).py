import sys
N = int(input())

n_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    n_list.append([int(age), name, i])

n_list.sort(key=lambda x:(x[0], x[2]))

for list in n_list:
    print(list[0], list[1])
