import sys

N, X = sys.stdin.readline().split()
N = int(N)
X = int(X)

xlist = sys.stdin.readline().split()

for i in xlist:
    if int(i) < X:
        print(i)
