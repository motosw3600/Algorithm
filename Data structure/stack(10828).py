import sys

class Stack:
    stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        val = 0
        if self.stack_list:
            print(self.stack_list[-1])
            del self.stack_list[-1]
        else:
            print(-1)


    def size(self):
        print(len(self.stack_list))

    def empty(self):
        if self.stack_list:
            print(0)
        else:
            print(1)

    def top(self):
        if self.stack_list:
            print(self.stack_list[-1])
        else:
            print(-1)

N = int(input())
stack = Stack()

for _ in range(N):
    in_com = sys.stdin.readline().rstrip().split()

    command = in_com[0]

    if command == 'push':
        stack.push(in_com[1])
    elif command == 'pop':
        stack.pop()
    elif command == 'size':
        stack.size()
    elif command == 'empty':
        stack.empty()
    elif command == 'top':
        stack.top()





