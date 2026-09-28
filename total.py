n = int(input())

for num in range(1, n + 1):
    temp = num
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    if total == 10:
        print(num, end=" ")