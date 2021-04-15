A, B = input().split()
sum = 0

lit_num = min(len(A), len(B))

for i in range(1, lit_num + 1):
    sum += (int(A[-i]) + int(B[-i])) * (10 ** (i - 1))

if len(B) > len(A):
    sum += int(B[:-i]) * (10 ** i)
elif len(A) > len(B):
    sum += int(A[:-i]) * (10 ** i)

print(sum)