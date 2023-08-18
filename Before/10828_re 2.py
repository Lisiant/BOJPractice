import sys


class Stack:

    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity
        self.idx = -1
        self.stack_size = 0

    def push(self, x: int):
        self.arr.append(x)
        self.idx += 1
        self.stack_size += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            x = self.arr.pop()
            self.stack_size -= 1
            self.idx -= 1
            return x

    def size(self):
        return self.stack_size

    def empty(self):
        if self.size() <= 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty():
            return -1
        else:
            x = self.arr[self.idx]
            return x


stack = Stack(10001)

tc = int(sys.stdin.readline())
for i in range(tc):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(stack.pop())
    elif cmd[0] == 'size':
        print(stack.size())
    elif cmd[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())
