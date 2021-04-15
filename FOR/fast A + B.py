import sys

count = int(sys.stdin.readline())

for _ in range(count):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(A + B)
