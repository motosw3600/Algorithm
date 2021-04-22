import sys
N = int(input())

stack = []
pm_list = []
tmp = 0
flag = True
for _ in range(N):
    inp = int(sys.stdin.readline())

    while tmp < inp:
        tmp += 1
        pm_list.append('+')
        stack.append(tmp)

    if stack[-1] == inp:
        pm_list.append('-')
        stack.pop()
    else:
        flag = False
        break


if flag == True:
    for i in pm_list:
        print(i)
else:
    print('NO')



