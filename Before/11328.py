import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    str1, str2 = sys.stdin.readline().split()
    str1 = sorted(list(str1))
    str2 = sorted(list(str2))
    is_possible = 1

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            is_possible = 0
            break

    if is_possible == 1:
        print("Possible")
    else:
        print("Impossible")
