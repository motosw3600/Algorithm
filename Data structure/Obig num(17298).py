N = int(input())

n_list = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(N)]

for i in range(N):
    while len(stack) != 0 and n_list[stack[-1]] < n_list[i]:
        answer[stack.pop()] = n_list[i]

    stack.append(i)

for x in answer:
    print(x, end=' ')