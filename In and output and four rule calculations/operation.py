a = input()
b = input()

sum = 0
leng = len(b)

for i in range(0, leng):
    print(int(a) * int(b[leng - i - 1]))
    sum += int(a) * int(b[leng - i - 1]) * (10 ** i)

print(sum)
