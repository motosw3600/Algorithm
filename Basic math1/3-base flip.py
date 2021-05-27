def solution(n):
    three_n = ""
    while n != 0:
        three_n += str(n % 3)
        n //= 3

    answer = int(three_n, 3)

    # for i in range(len(three_n)):
    #     answer += (int(three_n[-i-1]) * (3**i))

    return answer