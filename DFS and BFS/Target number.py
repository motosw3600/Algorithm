from collections import deque
answer = 0
def solution(numbers, target):
    return bfs(numbers, target)
    # dfs(numbers, target, 0)
    # return answer


def dfs(numbers, target, num):
    global answer
    if num == len(numbers) and target == 0:
        answer += 1
        return

    elif num == len(numbers):
        return

    dfs(numbers, target + numbers[num], num + 1)
    dfs(numbers, target - numbers[num], num + 1)


def bfs(numbers, target):
    answer = 0
    queue = deque([[0, 0]])
    length = len(numbers)
    while queue:
        val = queue.popleft()
        if val[0] < length:
            queue.append([val[0] + 1, val[1] + numbers[val[0]]])
            queue.append([val[0] + 1, val[1] - numbers[val[0]]])
        elif val[1] == target:
            answer += 1

    return answer