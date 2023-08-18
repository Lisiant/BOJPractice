test_case_num = int(input())

for _ in range(test_case_num):
    k = int(input())
    n = int(input())
    apt = [[0 for i in range(n)] for _ in range(k+1)]

    for i in range(n):
        apt[0][i] = i+1

    for i in range(1, k+1):
        for j in range(n):
            for h in range(j+1):
                apt[i][j] += apt[i-1][h]

    print(apt[k][n-1])
