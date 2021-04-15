import sys

count = 0
num = int(sys.stdin.readline())
check = num

while True:
    temp = num // 10 + num % 10
    s_num = (num % 10) * 10 + temp % 10
    count += 1
    num = s_num
    if check == s_num:
        break

print(count)

