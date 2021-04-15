T = int(input())

n_list = [0 for i in range(10001)]
for i in range(2, 101): # 소수인것은 0 아닌것은 1
    for j in range(i * 2, 10001, i):
        n_list[j] = 1

for _ in range(T):
    n = int(input())
    b = n // 2

    for k in range(b, 1, -1):
        if n_list[k] == 0 and n_list[n - k] == 0:
            print(k, n - k)
            break
