import sys
tc = int(sys.stdin.readline())

for i in range(tc):
    temp1 = []
    temp2 = []
    string = sys.stdin.readline().rstrip()

    for ch in string:

        if ch == '<':
            if len(temp1) == 0:
                continue
            else:
                temp2.append(temp1.pop())
        elif ch == '>':
            if len(temp2) == 0:
                continue
            else:
                temp1.append(temp2.pop())
        elif ch == '-':
            if len(temp1) == 0:
                continue
            else:
                temp1.pop()
        else:
            temp1.append(ch)

    if len(temp1) != 0:
        for ch in temp1:
            print(ch, end='')

    if len(temp2) != 0:
        for i in range(len(temp2)-1, -1, -1):
            print(temp2[i], end='')
    print()
