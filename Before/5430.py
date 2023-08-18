import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().rstrip()

    # 입력받은 문자열을 parsing 하는 다른 방법
    # data= sys.stdin.readline()[1:-2].split(',')

    is_error = 0
    cnt = 0

    arr = deque(list(data.lstrip('[').rstrip(']').split(',')))

    if arr[0] == '':
        arr.clear()

    arr = deque(map(int, arr))

    for i in range(len(cmd)):
        if cmd[i] == 'R':
            cnt += 1

        if cnt % 2 == 1:
            if cmd[i] == 'D':
                if len(arr) == 0:
                    is_error = 1
                    break
                else:
                    arr.pop()

        else:
            if cmd[i] == 'D':
                if len(arr) == 0:
                    is_error = 1
                    break
                else:
                    arr.popleft()

    if is_error == 1:
        print("error")
    else:
        if cnt % 2 == 1:
            string = "["+",".join(str(i) for i in reversed(arr)) + "]"
            print(string)
        else:
            string = "["+",".join(str(i) for i in arr) + "]"
            print(string)
