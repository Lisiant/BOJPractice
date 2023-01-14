n = int(input())
data = []

for i in range(n):
    age, name = input().split()
    age = int(age)

    data.append((age, i, name))


data.sort(key=lambda x: (x[0], x[1]))


for age, index, name in data:
    print(age, name)
