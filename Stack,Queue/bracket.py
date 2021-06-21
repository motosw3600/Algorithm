def solution(s):
    # stack사용
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)

        else:
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0