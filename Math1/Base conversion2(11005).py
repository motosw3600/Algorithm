N, B = map(int, input().split())

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''
while N != 0:
    answer += str(system[N % B])
    N //= B

print(answer[::-1])