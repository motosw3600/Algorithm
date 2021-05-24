def solution(answers):
    re_list = []
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    c_list = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == num_1[i % 5]:
            c_list[0] += 1
        if answers[i] == num_2[i % 8]:
            c_list[1] += 1
        if answers[i] == num_3[i % 10]:
            c_list[2] += 1

    max_val = max(c_list)

    for idx, val in enumerate(c_list):
        if val == max_val:
            re_list.append(idx + 1)

    return re_list