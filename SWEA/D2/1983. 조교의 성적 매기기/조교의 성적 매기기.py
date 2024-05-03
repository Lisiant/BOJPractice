grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())
for tc in range(1, t + 1):
    res = 0
    n, k = map(int, input().split())
    scores = []
    grades = [''] * (n + 1)
    rate = n // 10

    for i in range(1, n + 1):
        midterm, final, assignment = map(int, input().split())
        score = midterm * 0.35 + final * 0.45 + assignment * 0.20
        scores.append((score, i))

    scores.sort(key=lambda x: x[0], reverse=True)
    grade_idx = 0
    cnt = 0
    for i in range(n):
        if cnt == rate:
            grade_idx += 1
            cnt = 0

        grades[scores[i][1]] = grade_list[grade_idx]
        cnt += 1

    print(f"#{tc} {grades[k]}")
