n = 5

for i in range(n - 1, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        break