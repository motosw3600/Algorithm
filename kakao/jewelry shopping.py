def solution(gems):
    answer = []
    start_idx = 0
    end_idx = 0
    n_dic = {}
    length = len(set(gems))
    shortest = len(gems) + 1
    while end_idx < len(gems):

        if gems[end_idx] not in n_dic:
            n_dic[gems[end_idx]] = 1
        else:
            n_dic[gems[end_idx]] += 1

        end_idx += 1

        if len(n_dic) == length:
            while start_idx < end_idx:
                if n_dic[gems[start_idx]] > 1:
                    n_dic[gems[start_idx]] -= 1
                    start_idx += 1

                elif shortest > end_idx - start_idx:
                    shortest = end_idx - start_idx
                    answer = [start_idx + 1, end_idx]
                    break

                else:
                    break

    return answer