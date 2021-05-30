import heapq

def solution(scoville, K):
    cnt = 0
    heap = []

    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        cnt += 1

    print(cnt)
    return cnt

solution([1, 2, 3, 9, 10, 12], 7)