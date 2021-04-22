import sys
class Queue:
    q_list = []

    def push(self, val):
        self.q_list.append(val)

    def pop(self):
        if self.q_list:
            print(self.q_list.pop(0))
        else:
            print(-1)

    def size(self):
        print(len(self.q_list))

    def empty(self):
        if self.q_list:
            print(0)
        else:
            print(1)

    def front(self):
        if self.q_list:
            print(self.q_list[0])
        else:
            print(-1)

    def back(self):
        if self.q_list:
            print(self.q_list[-1])
        else:
            print(-1)

N = int(input())
queue = Queue()

for _ in range(N):
    inp = sys.stdin.readline()
    n_list = inp.rstrip().split()
    command = n_list[0]
    if command == 'push':
        queue.push(n_list[1])
    elif command == 'pop':
        queue.pop()
    elif command == 'size':
        queue.size()
    elif command == 'empty':
        queue.empty()
    elif command == 'front':
        queue.front()
    elif command == 'back':
        queue.back()
