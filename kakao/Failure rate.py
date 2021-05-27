def solution(N, stages):
    answer = []
    user = len(stages)
    n_dic = {}
    for i in range(1, N + 1):
        if user != 0:
            n_dic[i] = stages.count(i) / user
            user -= stages.count(i)
        else:
            n_dic[i] = 0

    n_dic = sorted(n_dic.items(), key=lambda x: (-x[1], x[0]))

    return list(map(lambda x: x[0], n_dic))