MAX = 100000
mod = 1000000009
dp =  [[0] * 4 for _ in range(MAX + 1)]

dp[0] = [0, 0, 0, 0]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]
n = int(input())

for i in range(4, MAX + 1):
    dp[i][1] = ((dp[i-1][2] + dp[i-1][3]) % mod)
    dp[i][2] = ((dp[i-2][1] + dp[i - 2][3]) % mod)
    dp[i][3] = ((dp[i - 3][1] + dp[i - 3][2]) % mod)

for _ in range(n):
    val = int(input())
    print(sum(dp[val]) % mod)

