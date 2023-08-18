import sys

while True:
    data = sorted(list(map(int, sys.stdin.readline().split())))
    a = data[0]
    b = data[1]
    c = data[2]

    if a == 0:
        break

    else:
        if (a**2) + (b**2) == (c**2):
            print("right")
        else:
            print("wrong")
