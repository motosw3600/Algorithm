def solution(array, commands):
    answer = []
    for arr in commands:
        n_list = array[arr[0] - 1:arr[1]]
        answer.append(sorted(n_list)[arr[2] - 1])
    return answer
    # return list(map(lambda a:sorted(array[a[0]-1:a[1]])[a[2]-1], commands))