def solution(n):
    answer = 0
    for i in range(1, n // 2 + 1):
        sum = i
        for j in range(i + 1, n // 2 + 2):
            sum += j
            if sum == n:
                answer += 1
            elif sum > n:
                break

    return answer + 1 if n > 0 else 0