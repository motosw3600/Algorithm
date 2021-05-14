n_list = []
for _ in range(9):
    n_list.append(int(input()))

n_list.sort()
sum_s = sum(n_list)

for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - n_list[i] - n_list[j] == 100:
            one = n_list[i]
            two = n_list[j]

n_list.remove(one)
n_list.remove(two)

for val in n_list:
    print(val)