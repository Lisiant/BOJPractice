import sys

string = sys.stdin.readline().rstrip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
temp = string

for croalp in cro:
    if croalp in temp:
        temp = temp.replace(croalp, '*')

        if croalp in temp:
            continue

print(len(temp))
