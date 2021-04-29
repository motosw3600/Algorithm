n = int(input())

n_card = [0]
n_card += list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]
dp[1] = n_card[1]
dp[2] = min(n_card[2], n_card[1] * 2)

for i in range(3, n + 1):
    dp[i] = n_card[i]
    for j in range(1, i//2 + 1):
        dp[i] = min(dp[i], dp[j] + dp[i - j])

print(dp[n])