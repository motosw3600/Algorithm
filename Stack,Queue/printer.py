from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque([[val, idx] for idx, val in enumerate(priorities)])
    while dq:
        val = dq.popleft()
        if len(dq) > 0 and val[0] < max([x[0] for x in dq]):
            dq.append(val)
        else:
            answer += 1
            if val[1] == location:
                break

    return answer