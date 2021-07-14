import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0
n_list = list(map(int,sys.stdin.readline().split()))

start_idx = 0
end_idx = 1
s = n_list[start_idx]

while end_idx <= n:
    s = sum(n_list[start_idx:end_idx])
    if s < m:
        end_idx += 1
    elif s == m:
        cnt += 1
        end_idx += 1
    else:
        start_idx += 1

print(cnt)