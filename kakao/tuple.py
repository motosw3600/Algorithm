def solution(s):
    answer = []
    n_list = s.split("},{")
    n_list[0] = n_list[0].replace("{{", "")
    n_list[-1] = n_list[-1].replace("}}", "")

    p_list = [list(map(int,x.split(','))) for x in n_list]

    for i in sorted(p_list, key=len):
        for k in i:
            if k not in answer:
                answer.append(k)
    # print(answer)
    return answer

# 정규식 풀이
# def solution(s):
#
#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
#
# import re
# from collections import Counter

solution("{{2},{2,1,3},{2,1},{2,1,3,4}}")

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")

solution("{{123}}")