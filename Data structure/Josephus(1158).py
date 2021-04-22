N, K = map(int, input().split())

n_list = [x+1 for x in range(N)]
print(n_list)

answer = []
S = 0

for _ in range(N):
    S += K - 1
    if S >= len(n_list):
        S = S % len(n_list)

    answer.append(str(n_list.pop(S)))

print('<', ", ".join(answer)[:],">", sep='')

