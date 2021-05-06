N = int(input())

p_line = list(map(int, input().split()))

sum = 0
wait_time = 0
for i in sorted(p_line):
    wait_time += i
    sum += wait_time

print(sum)