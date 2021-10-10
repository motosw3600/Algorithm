N = int(input())
for i in range(0, N):
    print(" "*i + "*"*((N-i)*2-1))

for i in range(N-2, -1, -1):
    print(" "*i + "*"*((N-i)*2-1))

# *****
#  ***
#   *
#  ***
# *****