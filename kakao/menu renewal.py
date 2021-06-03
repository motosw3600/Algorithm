# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     for c in course:
#         n_dic = {}
#         for i in orders:
#             p = list(combinations(i, c))
#             for k in p:
#                 string = "".join(sorted(k))
#                 if string in n_dic.keys():
#                     n_dic[string] += 1
#                 else:
#                     n_dic[string] = 1
#
#         if len(n_dic) > 0:
#             max_val = max(n_dic.values())
#             if max_val >= 2:
#                 for val in [x for x in n_dic.keys() if n_dic[x] == max_val]:
#                     answer.append(val)
#
#     return sorted(answer)


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
        print(result)
    return [ ''.join(v) for v in sorted(result) ]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])