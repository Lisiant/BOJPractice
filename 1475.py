n = input()
res = 0
count = [0 for i in range(9)]
six_or_nine = 0


for i in n:
    if i == '6' or i == '9':
        six_or_nine += 1
    else:
        count[int(i)] += 1


temp = max(count)

res += temp
six_or_nine = max(0, (six_or_nine // 2) + (six_or_nine % 2) - temp)
res += six_or_nine

print(res)
