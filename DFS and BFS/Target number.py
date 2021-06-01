cnt = 0
def solution(numbers, target):
    dfs(numbers, target, 0)
    return cnt

def dfs(numbers, target, num):
    global cnt

    if num == len(numbers) and target == 0:
        cnt += 1
        return

    if num == len(numbers):
        return

    dfs(numbers, target - numbers[num], num + 1)
    dfs(numbers, target + numbers[num], num + 1)