import sys

inp_n = int(sys.stdin.readline())

def iso_sequnce(n):
    count = 0
    for i in range(1, n+1):
        if i <= 99:
            count += 1
        else:
            i = str(i)
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                count += 1

    return  count

print(iso_sequnce(inp_n))