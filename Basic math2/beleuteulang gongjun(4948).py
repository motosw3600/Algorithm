def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

t_list = []

for i in range(2, 246912):
    if prime(i):
        t_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    s = 0
    for val in t_list:
        if n < val <= n*2:
            s += 1

    for i in range(n+1, 2 * n + 1):
        if i in t_list:
            s += 1
    print(s)
