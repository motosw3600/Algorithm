N = int(input())

print("*".rjust(N, " "))
for i in range(N - 2, -1, -1):
    print(" " * i + "*" + " " * ((N-i-1)*2-1) + "*")

#    *
#   * *
#  *   *
# *     *