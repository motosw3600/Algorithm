import sys
N = int(input())

n_list = []

for _ in range(N):
    n_list.append(int(sys.stdin.readline()))

for i in sorted(n_list):
    print(i)