from math import sqrt

while True:
    n_list = list(map(int, input().split()))
    if sum(n_list) == 0:
        break
    max_val = max(n_list)
    n_list.remove(max_val)

    if sqrt((n_list[0] ** 2) + (n_list[1] ** 2)) == max_val:
        print('right')
    else:
        print('wrong')
