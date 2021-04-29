n = int(input())

n_list = [0, 1, 2, 4]
for i in range(4, 11):
    n_list.append(sum(n_list[i - 3:i]))

for j in range(n):
    k = int(input())
    print(n_list[k])



