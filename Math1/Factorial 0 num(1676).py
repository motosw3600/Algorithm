N = int(input())

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

val = factorial(N)
num = 0
while val % 10 == 0:
    num += 1
    val = val // 10

print(num)