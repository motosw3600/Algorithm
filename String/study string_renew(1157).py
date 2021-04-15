word = input().upper()
unique_word = list(set(word))

a_list = []
for i in unique_word:
    a_list.append(word.count(i))

print(a_list)

if a_list.count(max(a_list)) > 2:
    print('?')
else:
    index = a_list.index(max(a_list))
    print(unique_word[index])

