import sys
input = sys.stdin.readline

data = list(map(str, input().rstrip()))
n = len(data)
res = [' '] * n
stk = []
tag = []
is_inside_tag = False

for i in range(n):

    if data[i] == '<':
        is_inside_tag = True
        res[i] = data[i]

        if len(stk) != 0:
            idx = stk[0][1]
            while stk:
                res[idx] = stk.pop()[0]
                idx += 1

    elif data[i] == '>':
        is_inside_tag = False
        res[i] = data[i]

    elif data[i] == ' ':
        if is_inside_tag:
            res[i] = data[i]
        else:
            idx = stk[0][1]
            while stk:
                res[idx] = stk.pop()[0]
                idx += 1
    else:
        if is_inside_tag:
            res[i] = data[i]
        else:
            stk.append((data[i], i))


if len(stk) != 0:
    idx = stk[0][1]
    while stk:
        res[idx] = stk.pop()[0]
        idx += 1

for ch in res:
    print(ch, end='')
