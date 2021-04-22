N = int(input())

for _ in range(N):
    n_list = input().split()
    for val in n_list:
        for i in range(len(val) - 1, -1, -1):
            print(val[i], end='')
        print(end=' ')
    print()