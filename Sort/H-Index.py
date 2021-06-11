def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# def solution(citations):
#     citations.sort()
#     h = 0
#     for i in range(0, len(citations) + 1):
#         if i > len([x for x in citations if x >= i]):
#             break
#         h = i
#
#     return h