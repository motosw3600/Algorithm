N = input()
n_list = []
for i in N:
    n_list.append(int(i))

for j in sorted(n_list,reverse=True):
    print(j, end='')

