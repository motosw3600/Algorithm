N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

c_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        c_sum[i][j] = arr[i-1][j-1] + c_sum[i-1][j] + c_sum[i][j-1] - c_sum[i-1][j-1]

K = int(input())
for _ in range(K):
    s1, s2, e1, e2 = list(map(int, input().split()))
    cumulSum = c_sum[e1][e2] - c_sum[e1][s2 - 1] - c_sum[s1 - 1][e2] + c_sum[s1-1][s2-1]
    print(cumulSum)