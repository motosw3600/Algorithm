list_a = []
list_b = []
for _ in range(3):
    x, y = map(int, input().split())
    list_a.append(x)
    list_b.append(y)

for i in range(3):
    if list_a.count(list_a[i]) == 1:
        r = list_a[i]
    if list_b.count(list_b[i]) == 1:
        t = list_b[i]

print(r, t)