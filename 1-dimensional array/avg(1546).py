import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
sum = 0

max_val = max(n_list)

for i in range(N):
    n_list[i] = n_list[i] / max_val * 100
    sum += n_list[i]

print(sum / N)
