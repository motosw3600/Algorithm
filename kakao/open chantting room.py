def solution(record):
    answer = []
    people = []
    dic = {}
    for i in record:
        re_val = i.split()
        if re_val[0] == "Enter":
            answer.append("님이 들어왔습니다.")
            people.append(re_val[1])
            dic[re_val[1]] = re_val[2]
        elif re_val[0] == "Leave":
            answer.append("님이 나갔습니다.")
            people.append(re_val[1])
        elif re_val[0] == "Change":
            dic[re_val[1]] = re_val[2]

    return [dic[p] + a for p, a in zip(people, answer)]