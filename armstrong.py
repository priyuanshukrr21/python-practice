n = int(input("Enter number: "))
original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong")