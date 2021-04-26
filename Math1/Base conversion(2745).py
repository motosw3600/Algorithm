N, B = input().split()

B = int(B)

cnt = 0
res = 0
for c in N:
    target = int(c) if c.isdigit() else ord(c) - 55
    res += (target * (B ** cnt))
    cnt += 1

print(res)

