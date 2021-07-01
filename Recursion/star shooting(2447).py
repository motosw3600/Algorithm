n = int(input())
star = [['*' for i in range(n)] for j in range(n)]

cnt = 0
v = n
while v != 1:
    v //= 3
    cnt += 1

for s in range(cnt):
    idx = [i for i in range(n) if ((i // (3 ** s))) % 3 == 1]

    for i in idx:
        for j in idx:
            star[i][j] = " "

for i in range(n):
    print("".join(star[i]))

# def get_stars(n):
#     matrix = []
#     for i in range(3 * len(n)):
#         if i // len(n) == 1:
#             matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
#         else:
#             matrix.append(n[i % len(n)] * 3)
#     return matrix
#
#
# star = ["***", "* *", "***"]
# n = int(input())
# e = 0
# while n != 3:
#     n = int(n / 3)
#     e += 1
#
# for i in range(e):
#     star = get_stars(star)
# for i in star:
#     print(i)





