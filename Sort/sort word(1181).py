import sys
N = int(input())

n_set = set()
for _ in range(N):
    n_set.add(sys.stdin.readline().strip())

for val in sorted(n_set, key=lambda x:(len(x), x)):
    print(val)
