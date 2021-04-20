import sys
import collections
N = int(input())

n_list = []
n_dic = collections.defaultdict(int)
for _ in range(N):
    val = int(sys.stdin.readline())
    n_list.append(val)
    n_dic[val] += 1

# 산술평균 출력
print(round(sum(n_list) / N))

# 중앙값 출력
n_list.sort()
print(n_list[len(n_list) // 2])

# 최빈값 출력
max_fre = max(n_dic.values())
fre_list = []
for i in n_dic.keys():
    if n_dic[i] == max_fre:
        fre_list.append(i)

if len(fre_list) < 2:
    print(fre_list[0])
else:
    fre_list.sort()
    print(fre_list[1])

# 범위 출력
print(n_list[-1] - n_list[0])




