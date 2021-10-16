import heapq
import sys

n = int(sys.stdin.readline())

input_list = []
n_list = []
val = 0

for _ in range(n):
    idx, start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(input_list, [start, end, idx])

start, end, num = heapq.heappop(input_list)
heapq.heappush(n_list, end)

while input_list:
    start, end, idx = heapq.heappop(input_list)
    if n_list[0] <= start:
        heapq.heappop(n_list)
    heapq.heappush(n_list, end)
    print(start, end)
    print(n_list)

print(len(n_list))
