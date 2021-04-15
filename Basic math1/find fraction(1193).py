N = int(input())

first = 1
plus = 1
sum = 1
flag = 1

if N == 1:
    print("1/1")
else:
    while True:
        if N < first:
            break
        else:
            first = first + plus
        sum += 1
        plus += 1
        flag *= -1

    print(f"first:{first} sum:{sum}")
    if flag == 1:
        print(f"{sum - first + N}/{first - N}")
    else:
        print(f"{first - N}/{sum - first + N}")