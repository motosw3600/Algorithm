from collections import Counter
def solution(participant, completion):
    answer = ''
    n_set = set(participant) - set(completion)
    if len(n_set) > 0:
        answer = n_set.pop()
    else:
        p_list = Counter(participant)
        n_list = Counter(completion)
        s_ans = p_list - n_list
        answer = s_ans.most_common(1)[0][0]
        print(answer)

    return answer

a = ['a', 'b', 'b', 'c']
b = ['a', 'b', 'c']
solution(a, b)
