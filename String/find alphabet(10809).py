import sys
import string

S = sys.stdin.readline().strip()
n_list = list(string.ascii_lowercase)
s_list = [-1 for i in range(len(n_list))]
n_dic = {key: value for key, value in zip(n_list, s_list)}

for i in range(0, len(S)):
    if n_dic[S[i]] == -1:
        n_dic[S[i]] = i

print(n for n in list(n_dic.values()))