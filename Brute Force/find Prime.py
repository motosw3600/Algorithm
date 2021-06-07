from itertools import permutations
import math


def isPrime(num):
    if num == 1:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    n_list = []
    for j in range(1, len(numbers) + 1):
        n_list += [int("".join(i)) for i in list(permutations(list(numbers), j)) if i[0] != '0' and int("".join(i)) > 1]

    return len(list(filter(isPrime, set(n_list))))