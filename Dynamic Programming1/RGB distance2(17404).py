import sys

n = int(input())
m = []
for _ in range(n):
    m.append([int(i) for i in sys.stdin.readline().split()])

ret = 1001 * 1001

for x in range(3):
    dp = [[0] * n for _ in range(3)]

    for i in range(3):
        if x == i:
            dp[i][0] = m[0][i]
        else:
            dp[i][0] = ret

    for i in range(1, n):
        dp[0][i] = m[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = m[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = m[i][2] + min(dp[0][i - 1], dp[1][i - 1])

    for i in range(3):
        if x == i:
            continue
        ret = min(ret, dp[i][-1])

print(ret)