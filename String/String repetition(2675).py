import sys
S = int(sys.stdin.readline())

for _ in range(S):
    R, P = sys.stdin.readline().split()
    str = ''

    for R_str in P:
        str += R_str * int(R)

    print(str)

