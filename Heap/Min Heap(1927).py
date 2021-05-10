import sys
import heapq

N = int(input())

heap = []
for _ in range(N):
    val = int(sys.stdin.readline())
    if val == 0:
        if len(heap) < 1:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, val)
