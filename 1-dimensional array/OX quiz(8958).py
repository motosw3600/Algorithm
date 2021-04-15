import sys

N = int(sys.stdin.readline())

for _ in range(N):
    count = 0
    O_count = 0
    for n in sys.stdin.readline():
        if n == 'O':
            O_count += 1
        else:
            O_count = 0
        count += O_count
    print(count)


