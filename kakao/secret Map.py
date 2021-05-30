def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        num1 = bin(arr1[i])[2:].zfill(n)
        num2 = bin(arr2[i])[2:].zfill(n)
        str = ""
        print(num1, num2)
        for j in range(n):
            if num1[j] == '1' or num2[j] == '1':
                str += "#"
            else:
                str += ' '
        answer.append(str)

    return answer

print("12345".rjust(6, "k"))