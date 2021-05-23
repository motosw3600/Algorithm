from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())

p_list = list(range(N))
S = [list(map(int, input().split())) for _ in range(N)]

min_val = 10000
for j in range(1, (N // 2) + 1):
    member_divide = list(combinations(p_list, j))

    for i in member_divide:
        start_list = list(i)
        link_list = list(set(p_list) - set(start_list))

        start = 0
        link = 0
        for k in range(N - 1):
            for j in range(N - 1):
                try:
                    start_sum = S[start_list[k]][start_list[j]]
                except IndexError:
                    start_sum = 0
                try:
                    link_sum = S[link_list[k]][link_list[j]]
                except:
                    link_sum = 0

                start += start_sum
                link += link_sum

        min_val = min(min_val, abs(start - link))
        if min_val == 0:
            print(min_val)
            exit()

print(min_val)

