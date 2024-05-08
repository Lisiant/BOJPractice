import sys

input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
store = int(input())
data = []
res = 0

for _ in range(store):
    d, cnt = map(int, input().split())
    data.append((d, cnt))

sdir, scnt = map(int, input().split())


def calc_distance(d, cnt):
    if sdir == d:
        return abs(scnt - cnt)

    if sdir == 1 or sdir == 2:
        sleft = scnt
        sright = n - scnt

        if d == 1 or d == 2:
            dleft = cnt
            dright = n - cnt

            return min(sleft + m + dleft, sright + m + dright)

        if d == 3 and sdir == 1:
            return sleft + cnt
        if d == 3 and sdir == 2:
            return sleft + m - cnt
        if d == 4 and sdir == 1:
            return sright + cnt
        if d == 4 and sdir == 2:
            return sright + m - cnt

    if sdir == 3 or sdir == 4:
        sup = scnt
        sdown = m - scnt

        if d == 3 or d == 4:
            return min(sup + n + cnt, sdown + n + m - cnt)

        if sdir == 3 and d == 1:
            return sup + cnt
        if sdir == 3 and d == 2:
            return sdown + cnt
        if sdir == 4 and d == 1:
            return sup + n - cnt
        if sdir == 4 and d == 2:
            return sdown + n - cnt


for d, cnt in data:
    res += calc_distance(d, cnt)
    
print(res)
