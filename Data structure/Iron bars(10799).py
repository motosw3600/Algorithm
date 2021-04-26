pip = input()

n_list = []
la_pip = ''
re_pip = 0
for i in pip:
    if i == '(':
        n_list.append(0)

    elif i == ')':
        if la_pip == '(':
            n_list.pop()
            re_pip += len(n_list)
        else:
            n_list.pop()
            re_pip += 1
    la_pip = i
print(re_pip)