n = int(input("Enter number: "))
even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print("Even =", even)
print("Odd =", odd)