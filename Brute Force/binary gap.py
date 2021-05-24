def solution(N):
    # write your code in Python 3.6
    by = bin(N)[2:]
    flag = False
    cnt = 0
    result = 0
    for i in by:
        if i == '1':
            flag = True
            if result < cnt:
                result = cnt
            cnt = 0
        elif i == '0' and flag == True:
            cnt += 1
    return result


