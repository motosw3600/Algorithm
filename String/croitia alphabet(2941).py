s = input()

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
i = 0
while i < len(s):
    if s[i:i+3] in cro_alpha:
        i += 3
        count += 1
        continue
    if s[i:i+2] in cro_alpha:
        i += 2
        count += 1
        continue
    i += 1
    count += 1

print(count)