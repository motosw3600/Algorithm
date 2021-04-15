import sys
import re

s = sys.stdin.readline()

regex = re.match(re.compile('[a-zA-Z]'), s)

print(regex)

if regex is None:
    print(chr(int(s)))
else:
    print(ord(s.strip()))