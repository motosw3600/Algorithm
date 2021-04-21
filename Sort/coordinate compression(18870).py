N = int(input())

n_list = list(map(int, input().split()))
s_list = sorted(list(set(n_list)))

s_dic = {s_list[i]:i for i in range(len(s_list))}

for i in n_list:
    print(s_list.index(i))
