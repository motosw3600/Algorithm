def solution(n):
    answer = ''
    num = ['1', '2', '4']
    while n != 0:
        print(n)
        answer = num[(n - 1) % 3] + answer
        n = (n - 1) // 3

    return answer