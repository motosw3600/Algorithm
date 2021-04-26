N = int(input())
n_list = list(map(int, input().split()))
n_dic = {}
for x in set(n_list):
    n_dic[x] = n_list.count(x)
answer = [-1 for _ in range(N)]
stack = []
for i in range(N):
    while len(stack) != 0 and n_dic[n_list[stack[-1]]] < n_dic[n_list[i]]:
        answer[stack.pop()] = n_list[i]
    stack.append(i)

print(answer)
