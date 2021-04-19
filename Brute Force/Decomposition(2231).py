N = int(input())

if N - (len(str(N))) * 9 < 0:
    s = N - (len(str(N)) - 1) * 9
else:
    s = N - (len(str(N))) * 9

while s < N:
    p = 0
    s = str(s)
    for i in range(len(s)):
        p += int(s[i])

    s = int(s)
    if N == s + p:
        break
    s += 1
else:
    s = 0

print(s)
