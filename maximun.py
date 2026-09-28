n = int(input("How many numbers: "))

maximum = -1
answer = 0

for i in range(n):
    num = int(input("Enter number: "))
    temp = num
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    if total > maximum:
        maximum = total
        answer = num

print("Number =", answer)
print("Digit Sum =", maximum)