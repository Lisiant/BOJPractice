import sys

n, k = map(int, sys.stdin.readline().split())
total = 0

student = [[0 for i in range(6)] for _ in range(2)]

for _ in range(n):
    is_man, grade = map(int, sys.stdin.readline().split())
    student[is_man][grade - 1] += 1

for i in range(2):
    for j in range(6):
        if student[i][j] == 0:
            continue

        if student[i][j] <= k:
            total += 1
        else:
            if student[i][j] % k == 0:
                total += student[i][j] // k
            else:
                total += (student[i][j] // k + 1)


print(total)
