import sys
import collections

in_str = sys.stdin.readline().upper().strip()
n_dic = collections.defaultdict(int)

for s in in_str:
    n_dic[s] += 1

dic_max = max(n_dic.values())

re_str = ''
count = 0
for i in n_dic:
    if n_dic[i] == dic_max:
        re_str = i
        count += 1

if count == 1:
    print(re_str)
else:
    print('?')