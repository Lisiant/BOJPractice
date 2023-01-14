import sys

stack = list(sys.stdin.readline().rstrip())
temp = list()
tc = int(sys.stdin.readline())

for _ in range(tc):

    cmd = sys.stdin.readline().split()

    if cmd[0] == 'P':
        stack.append(cmd[1])

    elif cmd[0] == 'L' and len(stack) != 0:
        temp.append(stack.pop())

    elif cmd[0] == 'D' and len(temp) != 0:
        stack.append(temp.pop())

    elif cmd[0] == 'B' and len(stack) != 0:
        stack.pop()


res = ''.join(stack)
res = res + ''.join(reversed(temp))
print(res)
