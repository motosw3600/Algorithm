T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    s = N % H * 100
    b = N // H + 1

    if N % H == 0:
        s = H * 100
        b -= 1

    print(s + b)


