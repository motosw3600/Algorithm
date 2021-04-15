N = int(input())

def first_prime(num):
    result = 0
    num = int(num ** 2) + 1
    for i in range(2, num):
        if num % i == 0:
            result = i
            break
    return result

while N > 1:
    s = first_prime(N)
    if s != 0:
        print(s)
        N = N // s
    else:
        print(N)
        break