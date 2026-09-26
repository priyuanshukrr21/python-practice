n = int(input("Enter number: "))
count = 0

while n > 0:
    n //= 10
    count += 1

print("Digits =", count)