from itertools import combinations
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0]) 

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)


# from itertools import combinations

# def solution(relation):
#     answer = set()
#     idx = [x for x in range(len(relation[0]))]
#     for i in range(1, len(idx) + 1):
#         combi = combinations(idx, i)
#
#         for val in combi:
#             flag = True
#             p_list = [""] * len(relation)
#             # if answer.issubset(set(val)):
#             #     print(val)
#             # flag = False
#             for k in val:
#                 for j in range(len(relation)):
#                     p_list[j] = p_list[j] + relation[j][k]
#
#             if len(p_list) == len(set(p_list)) and flag == True:
#                 answer.add(tuple(val))
#
#     print(answer)
#     return len(answer)