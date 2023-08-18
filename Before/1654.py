k, n = map(int, input().split())
lan_list = []
res = 0

for i in range(k):
    lan = int(input())
    lan_list.append(lan)

start = 0
end = max(lan_list)

while start <= end:
    tmp = 0
    tmp_num = 0

    mid = (start + end) // 2

    if mid != 0:
        for i in range(k):
            tmp_num = lan_list[i] // mid
            tmp += tmp_num
    else:
        res = 1
        break

    if tmp < n:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
