import sys
from collections import Counter

n = int(sys.stdin.readline())
data = []
sum_val = 0

for i in range(n):
    x = int(sys.stdin.readline())
    data.append(x)
    sum_val += x

data.sort()


def mean(arr):
    return round(sum_val / n)


def median(arr):
    return arr[n//2]


def most_common_num(arr):
    counter = Counter(data)
    m = counter.most_common()
    max_index = m[0][1]

    if len(m) == 1:
        return m[0][0]
    else:
        for i in range(len(m)-1):
            if m[i+1][1] != max_index:
                return m[0][0]
            else:
                return m[1][0]


def scope(arr):
    return max(arr) - min(arr)


print(mean(data))
print(median(data))
print(most_common_num(data))
print(scope(data))
