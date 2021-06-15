def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, val in enumerate(prices):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        else:
            stack.append(i)

    for _ in range(len(stack)):
        k = stack.pop()
        answer[k] = len(prices) - k - 1

    return answer
