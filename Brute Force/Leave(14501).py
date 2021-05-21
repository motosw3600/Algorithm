import sys
input = sys.stdin.readline
N = int(input())
s_list = [0 for i in range(N)]
p_list = [0 for i in range(N)]
max_list = [0 for i in range(N)]


for i in range(N):
    s_day, pay = map(int, input().split())
    s_list[i] = s_day
    p_list[i] = pay

# n을 더한것과 n+1중에 최댓값 max_list에 추가
for i in range(N - 1, -1, -1):
    val = 0
    if i + s_list[i] < N + 1:
        if i == N - 1 or i + s_list[i] == N:
            val = p_list[i]
        else:
            val = p_list[i]
            k = i
            k += s_list[i]
            val += max(max_list[k:])
    if i < N - 1:
        max_val2 = max(max_list[i + 1:])
    else:
        max_val2 = 0
    max_list[i] = max(val, max_val2)

print(max(max_list))