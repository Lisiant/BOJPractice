import sys


class Queue:

    def __init__(self, capacity: int):
        self.que = [None] * capacity
        self.capacity = capacity
        self.n = 0
        self.fr = 0
        self.rear = 0

    def empty(self):
        if self.n <= 0:
            return 1

        else:
            return 0

    def push(self, x: int):
        self.que[self.rear] = x
        self.rear += 1
        self.n += 1
        if self.rear == self.capacity:
            self.rear = 0

    def pop(self):
        if self.empty():
            return -1
        else:
            x = self.que[self.fr]
            self.fr += 1
            self.n -= 1
            if self.fr == self.capacity:
                self.fr = 0
            return x

    def size(self):
        return self.n

    def front(self):
        if self.empty():
            return -1
        else:
            return self.que[self.fr]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.que[self.rear - 1]


n = int(sys.stdin.readline().rstrip())
queue = Queue(n)


for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.push(command[1])
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    else:
        print(queue.back())
