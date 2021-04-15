N = int(input())

s = 2
while N > 1:
    if N % s == 0:
        print(s)
        N = N / s
    else:
        s += 1