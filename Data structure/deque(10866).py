import sys
from collections import deque
N = int(input())

class deq:
    def __init__(self):
        self.dq = deque()

    def push_front(self, num):
        self.dq.appendleft(num)

    def push_back(self, num):
        self.dq.append(num)

    def pop_front(self):
        if len(self.dq) > 0:
            print(self.dq.popleft())
        else:
            print(-1)

    def pop_back(self):
        if len(self.dq) > 0:
            print(self.dq.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.dq))

    def empty(self):
        if len(self.dq) > 0:
            print(0)
        else:
            print(1)

    def front(self):
        if len(self.dq) > 0:
            print(self.dq[0])
        else:
            print(-1)

    def back(self):
        if len(self.dq) > 0:
            print(self.dq[-1])
        else:
            print(-1)

dq = deq()
for _ in range(N):
    n_list = sys.stdin.readline().rstrip().split()

    command = n_list[0]
    if command == 'push_back':
        dq.push_back(n_list[1])
    elif command == 'push_front':
        dq.push_front(n_list[1])
    elif command == 'pop_front':
        dq.pop_front()
    elif command == 'pop_back':
        dq.pop_back()
    elif command == 'size':
        dq.size()
    elif command == 'empty':
        dq.empty()
    elif command == 'front':
        dq.front()
    elif command == 'back':
        dq.back()