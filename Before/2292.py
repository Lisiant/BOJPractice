n = int(input())
k = 1
while True:
    if n == 1:
        print(k)
        break
    elif n <= 1 + 3*k*(k+1):
        print(k+1)
        break
    else:
        k += 1
