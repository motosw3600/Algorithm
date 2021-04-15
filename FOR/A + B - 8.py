import sys

count = int(sys.stdin.readline())

for i in range(1, count + 1):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(f"Case #{i}: {A} + {B} = {A + B}")
