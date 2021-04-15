from string import ascii_lowercase

word = input()
alphabet = list(ascii_lowercase)  # 아스키코드 숫자 범위

print(alphabet)

for x in alphabet :
    print(word.find(x))

