from itertools import combinations
def solution(numbers):
    combination = list(combinations(numbers, 2))
    n_list = [sum(i) for i in combination]

    return sorted(list(set(n_list)))