x, y = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

val = gcd(x, y)
print(val)
print(val * x//val * y//val)

