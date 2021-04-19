def hanoi(s, n, N):
    if N < 2:
        print(s, n)
    else:
        k = 6 - s - n
        hanoi(s, k, N - 1)
        print(s, n)
        hanoi(k, n, N - 1)

N = int(input())

sum = 1
for i in range(N-1):
    sum = sum * 2 + 1

print(sum)
hanoi(1, 3, N)
