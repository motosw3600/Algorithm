n = int(input())
# 경우의 수 왼쪽에만 있을 때 오른쪽에만 있을 때 아무것도 없을 때
s = [[0] * 3 for i in range(100001)]
for i in range(3):
    s[1][i] = 1
for i in range(2, n+1):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901
print(sum(s[n]) % 9901)