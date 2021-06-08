def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    n_list = [[1, yellow]]
    i = 2
    while i < yellow // 2 + 1:
        if yellow % i == 0:
            n_list.append([i, yellow // i])
        i += 1

    for val in n_list:
        a = val[0] + 2
        b = val[1] + 2
        if a * b == sum:
            if b > a:
                a, b = b, a
            answer.append(a)
            answer.append(b)
            break

    return answer