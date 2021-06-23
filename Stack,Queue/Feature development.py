from math import ceil


def solution(progresses, speeds):
    stack = []
    for p, s in zip(progresses, speeds):
        if len(stack) == 0 or stack[-1][0] < ceil((100 - p) / s):
            stack.append([ceil((100 - p) / s), 1])
        else:
            stack[-1][1] += 1

    return [s[1] for s in stack]