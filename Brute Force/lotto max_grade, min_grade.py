def solution(lottos, win_nums):
    answer = []

    zero_cnt = lottos.count(0)

    dif_lottos = set(lottos) - set(win_nums) - {0}

    answer.append(min(6, 1 + len(dif_lottos)))
    answer.append(min(6, 1 + len(dif_lottos) + zero_cnt))

    return answer