import sys


class Queue:

    def __init__(self, capacity):
        self.arr = list()
        self.capacity = capacity
        self.n = 0
        self.front_idx = 0
        self.rear_idx = 0

    def push(self, x: int):
        self.arr.append(x)
        self.rear_idx += 1
        self.n += 1

    def pop(self):
        if self.empty():
            return -1
        x = self.arr.pop(0)
        self.n -= 1
        self.rear_idx -= 1
        return x

    def size(self):
        return self.n

    def empty(self):
        if self.n <= 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.front_idx]

    def back(self):
        if self.empty():
            return -1

        else:
            return self.arr[self.rear_idx - 1]


tc = int(sys.stdin.readline())
queue = Queue(tc)

for _ in range(tc):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.empty())
    elif cmd[0] == 'front':
        print(queue.front())
    else:
        print(queue.back())
