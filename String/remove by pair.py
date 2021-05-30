def solution(s):
    i = 0
    stack = []

    for i in s:
        if stack[-1:] == [i]:
            stack.pop()
        else:
            stack.append(i)

    return 0 if len(stack) > 0 else 1