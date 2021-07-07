def solution(lines):
    answer = []
    log = []
    for line in lines:
        data = line.split()
        date = list(map(float, data[1].split(":")))
        s = date[2] + date[1] * 60 + date[0] * 3600
        t = float(data[2][:-1])

        start_log = round(s - t + 0.001, 4)
        if start_log < 0:
            start_log = 0
        log.append([start_log, s])

    time = []
    for i in log:
        time += i

    for val in time:
        cnt = 0
        start = val
        end = round(val + 1 - 0.001, 4)
        for p in log:
            if start <= p[0] <= end or start <= p[1] <= end:
                cnt += 1
            elif p[0] <= start <= p[1] and p[0] <= end <= p[1]:
                cnt += 1
            answer.append(cnt)

    return max(answer)