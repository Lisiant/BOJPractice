import sys
from collections import deque


def pop_element(queue: deque):
    x = queue.popleft()
    return x


def left_rotate(queue: deque):
    queue.append(queue.popleft())


def right_rotate(queue: deque):
    queue.appendleft(queue.pop())


n, m = map(int, sys.stdin.readline().split())
data = deque(map(int, sys.stdin.readline().split()))
circular_queue = deque(list(map(int, range(1, n+1))))
result = 0
temp = data[0]

while True:

    if circular_queue[0] == temp:
        x = pop_element(circular_queue)
        data.popleft()

        if len(data) == 0:
            print(result)
            break
        else:
            temp = data[0]

    if (circular_queue.index(temp)) <= len(circular_queue) - 1 - circular_queue.index(temp):
        left_rotate(circular_queue)
        result += 1

    else:
        right_rotate(circular_queue)
        result += 1
