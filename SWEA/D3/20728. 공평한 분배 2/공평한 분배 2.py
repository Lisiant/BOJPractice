t = int(input())
INF = int(1e9)
for tc in range(1, t + 1):

    n, k = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    res = INF

    if n == k:
        res = min(data[n - 1] - data[0], res)

    for i in range(n - k + 1):
        res = min(res, data[i + k - 1] - data[i])

    print(f"#{tc} {res}")
