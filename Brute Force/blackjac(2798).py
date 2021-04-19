N, M = map(int, input().split())
c_list = list(map(int,input().split()))

max_val = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = c_list[i] + c_list[j] + c_list[k]
            if sum <= M and sum >= max_val:
                max_val = sum

print(max_val)

