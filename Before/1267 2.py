def youngsik(n):
    val = ((n // 30) + 1) * 10
    return val


def minsik(n):
    val = ((n // 60) + 1) * 15
    return val


n = int(input())
data = list(map(int, input().split()))
y = m = 0

for i in range(n):
    y += youngsik(data[i])
    m += minsik(data[i])

if y > m:
    print("M {}".format(m))
elif y < m:
    print("Y {}".format(y))
else:
    print("Y M {}".format(y))
