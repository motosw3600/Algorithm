A, B = map(int, input().split())
N = int(input())
S_list = list(map(int, input().split()))

res = 0
answer = []

for i in range(N):
    res += (S_list[-1] * (A ** i))
    S_list.pop(-1)

while res != 0:
    answer.append(str(res % B))
    res //= B

print(' '.join(answer[::-1]))

