def chk_group(word):
    a_list = []
    flag = word[0]
    for i in word:
        if i not in a_list:
            a_list.append(i)
        else:
            if flag != i:
                return None
        flag = i
    return True

N = int(input())
count = 0
for _ in range(N):
    s = input()
    if chk_group(s) is not None:
        count += 1

print(count)
