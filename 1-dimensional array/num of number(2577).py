A = int(input())
B = int(input())
C = int(input())

list = [0 for i in range(10)]

for j in str(A * B * C):
    list[int(j)] += 1

for i in list:
    print(i)
