a = int(input("Base: "))
b = int(input("Power: "))

result = 1

for i in range(b):
    result *= a

print("Answer =", result)