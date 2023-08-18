import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    data = list(map(int, sys.stdin.readline().split()))
    student_num = data.pop(0)
    avg = sum(data) / student_num

    over_avg_student = 0
    for student in data:
        if student > avg:
            over_avg_student += 1
    print("{:.3f}%".format((over_avg_student / student_num) * 100))
