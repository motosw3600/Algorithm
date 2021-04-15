_set = set()

for _ in range(0, 10):
    num = int(input())
    _set.add(num % 42)

print(len(_set))