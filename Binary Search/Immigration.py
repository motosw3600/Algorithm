def solution(n, times):
    s = 1
    e = max(times) * n
    min_time = 0

    while s <= e:
        mid = (s + e) // 2
        people = 0
        for i in range(len(times)):
            people += mid // times[i]
            if people >= n:
                break

        if people >= n:
            min_time = mid
            e = mid - 1
        else:
            s = mid + 1

    return min_time