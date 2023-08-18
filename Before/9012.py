import sys
tc = int(sys.stdin.readline())

for i in range(tc):
    is_vps = True
    stk = list()
    ps = sys.stdin.readline().rstrip()

    for i in range(len(ps)):
        if len(stk) == 0:
            if ps[i] == '(':
                stk.append(ps[i])
            else:
                is_vps = False
                break
        else:
            if ps[i] == '(':
                stk.append(ps[i])
            else:
                stk.pop()

    if is_vps == True and len(stk) == 0:
        print("YES")
    else:
        print("NO")
