def phibonachi(n):
    if n < 2:
        return n

    return phibonachi(n-1) + phibonachi(n-2)

print(phibonachi(10))