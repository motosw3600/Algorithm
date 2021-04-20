import sys

N = int(input())
n_list = []
c_list = [0 for i in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    c_list[num] += 1

for i in range(1, 10001):
    val = c_list[i]
    for _ in range(val):
        print(i)

