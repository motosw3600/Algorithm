def solution(brown, yellow):
    answer = []
    sum = brown + yellow

    for i in range(3, sum // 2 + 1):
        j = sum // i
        if (i - 2) * (j - 2) == yellow:
            answer = [j, i]
            break

    return answer