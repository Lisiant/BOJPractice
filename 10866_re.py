from collections import deque
import sys


class Boj_10866:

    def __init__(self):
        self.deq = deque()
        self.n = 0

    def push_front(self, x):
        self.deq.appendleft(x)
        self.n += 1

    def push_back(self, x):
        self.deq.append(x)
        self.n += 1

    def pop_front(self):
        if self.empty():
            return -1

        x = self.deq.popleft()
        self.n -= 1
        return x

    def pop_back(self):
        if self.empty():
            return -1

        x = self.deq.pop()
        self.n -= 1
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
            x = self.deq.popleft()
            self.deq.appendleft(x)
            return x

    def back(self):
        if self.empty():
            return -1
        else:
            x = self.deq.pop()
            self.deq.append(x)
            return x


n = int(sys.stdin.readline())
deque = Boj_10866()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        deque.push_front(int(cmd[1]))

    elif cmd[0] == 'push_back':
        deque.push_back(int(cmd[1]))

    elif cmd[0] == 'pop_front':
        print(deque.pop_front())

    elif cmd[0] == 'pop_back':
        print(deque.pop_back())

    elif cmd[0] == 'size':
        print(deque.size())

    elif cmd[0] == 'empty':
        print(deque.empty())

    elif cmd[0] == 'front':
        print(deque.front())

    else:
        print(deque.back())
