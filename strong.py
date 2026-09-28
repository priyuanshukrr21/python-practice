n = int(input())
original = n
total = 0

while n > 0:
    digit = n % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total += fact
    n //= 10

if total == original:
    print("Strong Number")
else:
    print("Not Strong")