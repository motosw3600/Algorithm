n_list = input()

flag = True
m_list = []

for i in n_list:
    if i == '<':
        flag = False
    if i == '>':
        print(i, end='')
        flag = True
        continue

    if i == ' ' or i == '<' and len(m_list) > 0 :
        m_list.reverse()
        print("".join(m_list), end='')
        m_list.clear()

    if flag == False:
        print(i, end='')
    else:
        if i != ' ':
            m_list.append(i)
        else:
            print(i, end='')

if len(m_list) > 0:
    m_list.reverse()
    print("".join(m_list))


