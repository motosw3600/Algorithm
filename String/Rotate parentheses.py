from collections import deque

def solution(s):
    cnt = 0
    string = deque(s)
    for _ in range(len(s)):
        string.rotate(-1)
        cnt += chkString(string)

    return cnt

def chkString(string):
    stack = []
    for s in string:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        elif s == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif s == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0

    return 1 if len(stack) == 0 else 0