import sys
from collections import deque


class Deq:

    def __init__(self, capacity: int):
        self.q = deque(maxlen=capacity)

    def push_front(self, x):
        self.q.appendleft(x)

    def push_back(self, x):
        self.q.append(x)

    def pop_front(self):
        if self.size() <= 0:
            return -1
        else:
            return self.q.popleft()

    def pop_back(self):
        if self.size() <= 0:
            return -1
        else:
            return self.q.pop()

    def size(self):
        return len(self.q)

    def empty(self):
        if self.size() <= 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() <= 0:
            return -1
        else:
            x = self.q.popleft()
            self.q.appendleft(x)
            return x

    def back(self):
        if self.size() <= 0:
            return -1
        else:
            x = self.q.pop()
            self.q.append(x)
            return x


n = int(sys.stdin.readline().rstrip())
d = Deq(10001)

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        d.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        d.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        print(d.pop_front())
    elif cmd[0] == 'pop_back':
        print(d.pop_back())
    elif cmd[0] == 'size':
        print(d.size())
    elif cmd[0] == 'empty':
        print(d.empty())
    elif cmd[0] == 'front':
        print(d.front())
    else:
        print(d.back())
