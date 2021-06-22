def solution(files):
    answer = []
    # 1. Header기중
    # 2. Header같으면 number기준
    # 3. Header, number모두 같으면 먼저 입력된 순(인덱스 저장해놓거나 인식해서 인덱스로 정렬)

    i_files = [[*seperate(val.upper()), i] for i, val in enumerate(files)]
    i_files.sort(key=lambda x: (x[0], x[1], x[2]))
    print(i_files)

    return [files[x[2]] for x in i_files]

def seperate(s):
    num = ''
    string = ''
    for i in s:
        if i.isdigit():
            num += i
        else:
            if num != '':
                break
            string += i

    return string, int(num)

# 정규식
# import re
#
# def solution(files):
#     a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
#     b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
#     return b
