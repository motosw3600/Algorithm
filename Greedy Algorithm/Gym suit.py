def solution(n, lost, reserve):
    answer = 0

    reserve, lost = list(set(reserve) - set(lost)), list(set(lost) - set(reserve))
    # O(n^2)
    #     answer = n - len(lost)

    #     for i in range(len(reserve)):
    #         for j in range(len(lost)):
    #             if abs(reserve[i] - lost[j]) == 1:
    #                 answer += 1
    #                 reserve[i] = 100
    #                 lost[j] = 100

    # O(n)
    for i in reserve:
        f = i + 1
        b = i - 1
        if b in lost:
            lost.remove(b)
        elif f in lost:
            lost.remove(f)

    return n - len(lost)