def star(n: int):
    if n < 3:
        return 0
    k = n // 3
    if k < 2:
        print(n * "*")
        print(k  * "*"+ k *' ' + k * "*")
        print(n * "*")


N = int(input())

star(N)


# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********
