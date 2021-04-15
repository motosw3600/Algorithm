X = int(input())

line = 1


while X - line > 0:
    X = X - line
    line += 1

print(X, line)

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(f"{a}/{b}")