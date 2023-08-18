import sys


class Stack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr

    def is_empty(self):
        return bool(self.ptr <= 0)

    def is_full(self):
        return bool(self.ptr >= self.capacity)

    def push(self, x: int):
        if self.is_full():
            return Stack.Full
        else:
            self.stk[self.ptr] = x
            self.ptr += 1

    def pop(self):
        if self.is_empty():
            return -1
        else:
            self.ptr -= 1
            return self.stk[self.ptr]

    def size(self):
        return self.__len__()

    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0

    def top(self):
        if self.is_empty():
            return -1
        else:
            return self.stk[self.ptr - 1]


n = int(sys.stdin.readline().rstrip())
stack = Stack(n)

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())

    elif command[0] == 'size':
        print(stack.size())

    elif command[0] == 'empty':
        print(stack.empty())

    else:
        print(stack.top())
