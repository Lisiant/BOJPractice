import sys

input = sys.stdin.readline

data = list(map(str, input().rstrip()))
dic = {
    'C': 12,
    'H': 1,
    'O': 16
}
stk = []
temp = 0

for i in range(len(data)):
    if data[i] in dic.keys():
        stk.append(dic[data[i]])
    elif data[i] == '(':
        stk.append(data[i])
    elif data[i] == ')':

        while True:
            val = stk.pop()

            if val == '(':
                break

            temp += val
        stk.append(temp)
        temp = 0
    else:
        num = int(data[i])
        stk[-1] *= num

print(sum(stk))
