import sys
N = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
s_list = list(map(int, sys.stdin.readline().split()))

def binary_search(num, f_list, s_idx = 0, e_idx = None):

    if e_idx == None:
        e_idx = len(f_list) - 1

    if s_idx == e_idx and f_list[s_idx] != num:
        if f_list[s_idx] != num:
            return 0
        else:
            return 1

    mid_index = (s_idx + e_idx) // 2

    if f_list[mid_index] == num:
        return 1
    elif f_list[mid_index] < num:
        return binary_search(num, f_list, mid_index + 1, e_idx)
    elif f_list[mid_index] > num:
        return binary_search(num, f_list, s_idx, mid_index)
    else:
        return 0


n_list.sort()
for i in s_list:
    print(binary_search(i, n_list))