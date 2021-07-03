# 10 -> 2
def bin_conversion(n):
    num = ""
    while n != 0:
        num += str(n%2)
        n //= 2

    return num[::-1]

# 10 -> 8
def oct_conversion(n):
    num = ""

    while n != 0:
        num += str(n%8)
        n //= 8

    return num[::-1]

# 10 -> 16
def hex_conversion(n):
    num = ""
    hex_str = "0123456789ABCDEF"
    while n != 0:
        num += hex_str[n % 16]
        n //= 16

    return num[::-1]

# base -> 10
def int_conversion(base, n):
    num = 0
    for i, v in enumerate(str(n)[::-1]):
        num += (base**i) * int(v)

    return num


print(bin_conversion(4))
print(oct_conversion(9))
print(hex_conversion(16))
print(int_conversion(2, 1011))
