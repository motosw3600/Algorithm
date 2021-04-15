def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

N = int(input())

n_list = list(map(int, input().split()))

for i in range(0 ,len(n_list)):
    a = n_list[i] - 1
    if n_list[i] == 1:
        N -= 1
    else:
        while a > 1:
            if n_list[i] % a == 0:
                N -= 1
                break
            a -= 1

print(N)