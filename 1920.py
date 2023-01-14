n = int(input())
data = sorted(list(map(int, input().split())))

m = int(input())
val = list(map(int, input().split()))
result = []


def binary_search(arr, key: int):
    pl = 0
    pr = len(arr) - 1

    while True:
        pc = (pl + pr) // 2

        if arr[pc] == key:
            return 1

        elif arr[pc] < key:
            pl = pc + 1

        else:
            pr = pc - 1

        if pl > pr:
            return 0


for item in val:
    result.append(binary_search(data, item))


for ans in result:
    print(ans)
