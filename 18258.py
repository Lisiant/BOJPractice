import sys
from collections import deque


class Q:

    def __init__(self, capacity):
        self.q = deque(maxlen=capacity)
        self.capacity = capacity
        self.front_idx = 0
        self.rear_idx = 0
        self.qlen = 0

    def push(self, x: int):
        self.q.append(x)
        self.qlen += 1
        self.rear_idx += 1

    def pop(self):

        if self.empty():
            return -1

        x = self.q.popleft()
        self.qlen -= 1
        self.rear_idx -= 1
        return x

    def size(self):
        return self.qlen

    def empty(self):
        if self.size() <= 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.q[self.front_idx]

    def back(self):
        if self.empty():
            return -1

        else:
            return self.q[self.rear_idx - 1]


n = int(sys.stdin.readline())
que = Q(2000001)

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        que.push(cmd[1])
    elif cmd[0] == 'pop':
        print(que.pop())
    elif cmd[0] == 'size':
        print(que.size())
    elif cmd[0] == 'empty':
        print(que.empty())
    elif cmd[0] == 'front':
        print(que.front())
    elif cmd[0] == 'back':
        print(que.back())
