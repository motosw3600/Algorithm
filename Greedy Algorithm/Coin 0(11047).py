N, money = map(int, input().split())
m_list = []
for _ in range(N):
    m_list.append(int(input()))
cnt = 0

for i in range(N - 1, -1, -1):
    if money / m_list[i] != 0:
        cnt += money // m_list[i]
        money = money % m_list[i]
    if money == 0:
        break


print(cnt)
