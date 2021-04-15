N = int(input())
a = 0
b = 0

for i in range(((N // 5)), -1, -1):
    if N - 5 * i != 0:
        if (N - 5 * i) % 3 == 0:
            a = i
            b = (N - 5 * i) // 3
            break
    else:
        a = i
        break

if a != 0 or b != 0:
    print(a+b)
else:
    print(-1)