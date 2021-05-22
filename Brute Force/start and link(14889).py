from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
player = [i for i in range(N)]
S = [list(map(int, input().split())) for _ in range(N)]

p_list = list(combinations(player, N // 2))

min_val = 10000
for i in range(len(p_list) // 2):
    # team A
    start = 0
    team_A = p_list[i]
    for k in team_A:
        for j in team_A:
            start += S[k][j]

    # team B
    link = 0
    team_B = p_list[-i - 1]
    for k in team_B:
        for j in team_B:
            link += S[k][j]

    min_val = min(min_val, abs(start - link))

print(min_val)