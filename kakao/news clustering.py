import re
import math
def solution(str1, str2):
    answer = 0
    regex = re.compile('[a-zA-Z]')
    divide1 = []
    divide2 = []
    for i in range(len(str1) - 1):
        if regex.match(str1[i]) is not None and regex.match(str1[i + 1]) is not None:
            divide1.append((str1[i] + str1[i + 1]).upper())

    for i in range(len(str2) - 1):
        if regex.match(str2[i]) is not None and regex.match(str2[i + 1]) is not None:
            divide2.append((str2[i] + str2[i + 1]).upper())

    inter = 0

    for i in range(len(divide1)):
        for j in range(len(divide2)):
            if divide1[i] == divide2[j]:
                inter += 1
                divide2[j] = 0
                break

    if len(divide1) == 0 and len(divide2) == 0:
        answer = 65536
    else:
        answer = math.floor((inter / (len(divide1) + len(divide2) - inter)) * 65536)
    return answer