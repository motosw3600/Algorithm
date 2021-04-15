M = int(input())
N = int(input())

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n_list = []

for i in range(M, N + 1):
    if prime(i):
        n_list.append(i)


if n_list:
    print(sum(n_list))
    print(min(n_list))
else:
    print(-1)