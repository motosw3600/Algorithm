S = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

d_sum = 0
for i in S:
    for j in range(len(dial)):
        if i in dial[j]:
            d_sum += j + 3
print(d_sum)