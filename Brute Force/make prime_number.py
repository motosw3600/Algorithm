from itertools import combinations
def solution(nums):
    answer = 0
    n_list = [prime_number(sum(c)) for c in combinations(nums, 3)]

    return sum(n_list)

def prime_number(num):
    cnt = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            cnt += 1
    return 0 if cnt > 0 else 1