import sys

N, Q = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
arr = [0] + n_list

def search(s, e, k):
    while s < e:
        mid = (s + e) // 2
        if arr[mid] >= k:
            s = mid + 1
        else:
            e = mid
    return s

for i in range(Q):
    x, y = map(int, sys.stdin.readline().split())
    tmp = search(1, N, x)

    res = 1 if arr[N] >= x else 0
    if arr[y] - x < 0 or tmp - y < 0:
        print(0)
    else:
        print(arr[y] - x + tmp - y + res)



