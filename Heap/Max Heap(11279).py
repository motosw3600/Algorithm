import sys
import heapq

N = int(input())
n_heap = []

for _ in range(N):
    inp = int(sys.stdin.readline())
    heapq.heappush(n_heap, (-inp, inp))

    if inp == 0:
        if len(n_heap) > 0:
            print(heapq.heappop(n_heap)[1])
        else:
            print(0)



