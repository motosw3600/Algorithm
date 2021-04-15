import sys

while True:
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    if A == 0 and B == 0:
        break;
    print(A + B)


