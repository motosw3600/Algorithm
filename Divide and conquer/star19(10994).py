N = int(input())
m = 4 * (N-1) + 1
n_list = [["*" for _ in range(m)] for _ in range(m)]
leng = len(n_list)

def recursive(n, k):
    if n == 1:
        return
    for i in range(k, leng - k):
        n_list[i][k] = " "
        n_list[i][leng - k - 1] = " "
        n_list[k][i] = " "
        n_list[leng - k - 1][i] = " "
    recursive(n - 4, k+2)

recursive(m, 1)

for val in n_list:
    print("".join(val))

# *****
# *   *
# * * *
# *   *
# *****

# *********
# *       *
# * ***** *
# * *   * *
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********

# *************
# *           *
# * ********* *
# * *       * *
# * * ***** * *
# * * *   * * *
# * * * * * * *
# * * *   * * *
# * * ***** * *
# * *       * *
# * ********* *
# *           *
# *************
