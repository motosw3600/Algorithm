def d(n):
    con_num = n
    while n // 10 != 0:
        con_num += n % 10
        n = n // 10
    con_num += n

    return con_num

n_list = list(map(d, [x for x in range(1, 10000)]))

for i in range(1, 10000):
    if i not in n_list:
        print(i)
