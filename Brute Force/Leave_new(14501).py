import sys
input = sys.stdin.readline
N = int(input())
s_list = [0 for i in range(N)]
p_list = [0 for i in range(N)]
max_list = [0 for i in range(N + 1)]


for i in range(N):
    s_day, pay = map(int, input().split())
    s_list[i] = s_day
    p_list[i] = pay

# n을 더한것과 n+1중에 최댓값 max_list에 추가
for i in range(N - 1, -1, -1):
    if i + s_list[i] > N:
        max_list[i] = max_list[i + 1]
    else:
        max_list[i] = max(max_list[i + 1], p_list[i] + max_list[i + s_list[i]])

print(max_list)
print(max_list[0])