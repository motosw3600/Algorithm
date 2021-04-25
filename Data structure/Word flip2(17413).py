n_list = input()

flag = False
m_word = ''
re_str = ''

for i in n_list:
    if flag == False:
        if i == '<':
            re_str += i
            flag = True
        elif i == ' ':
            re_str += m_word + ' '
            m_word = ''
        else:
            m_word = i + m_word

    elif flag == True:
        re_str += i
        if i == '>':
            tag = False

print(re_str)




