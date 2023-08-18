a, b, v = map(int, input().split())
val = (v-b)/(a-b)

if (v-b) % (a-b) == 0:
    print(int(val))
else:
    print(int(val)+1)
