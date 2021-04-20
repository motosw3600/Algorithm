N = int(input())

n_list = []

for _ in range(N):
    n_list.append(int(input()))

def merge(a_list, b_list):
    re_list = []
    a = 0
    b = 0

    while a < len(a_list) and b < len(b_list):
        if a_list[a] < b_list[b]:
            re_list.append(a_list[a])
            a += 1
        else:
            re_list.append(b_list[b])
            b += 1

    if a == len(a_list):
        re_list = re_list + b_list[b:]
    else:
        re_list = re_list + a_list[a:]

    return re_list


def merge_sort(p_list):
    if len(p_list) < 2:
        return p_list

    mid_idx = len(p_list) // 2

    return merge(merge_sort(p_list[:mid_idx]), merge_sort(p_list[mid_idx:]))

n_list = merge_sort(n_list)

for i in n_list:
    print(i)
