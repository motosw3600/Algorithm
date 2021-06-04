from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx, val in enumerate(priorities):
        queue.append([val, idx])
    answer = 0
    cnt = 0
    while queue:
        val = queue.popleft()
        if len(queue) > 0 and val[0] < max([x[0] for x in queue]):
            queue.append(val)
        else:
            cnt += 1
            if val[1] == location:
                answer = cnt
                break

    return answer