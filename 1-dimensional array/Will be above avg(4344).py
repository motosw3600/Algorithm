import sys

C = int(sys.stdin.readline())

for _ in range(C):
    avg_up = 0
    n_list = list(map(int, sys.stdin.readline().split()))
    avg = sum(n_list[1:])/n_list[0]
    for i in range(1, len(n_list)):
        if n_list[i] > avg:
            avg_up += 1

    print(f"{avg_up/n_list[0] * 100:.3f}%")

