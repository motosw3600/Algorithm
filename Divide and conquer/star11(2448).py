N = int(input())

n_list = [[" " for _ in range(N*2-1)] for _ in range(N)]

def recursive(k, n, p):
    n_list[k][n-1] = "*"
    n_list[k+1][n-2] = "*"
    n_list[k+1][n] = "*"
    for i in range(n-3, n+2):
        n_list[k+2][i] = "*"

    if p == 3:
        return
    recursive(k, n, p//2 )
    recursive(k+p//2, n - p//2, p//2)
    recursive(k+p//2, n + p//2, p//2)

recursive(0, N, N)

for val in n_list:
    print("".join(val))


#   *
#  * *
# *****

#      *
#     * *
#    *****
#   *     *
#  * *   * *
# ***** *****

