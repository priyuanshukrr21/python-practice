a = 20
b = 4

q = 0

while a >= b:
    a = a ^ b
    q = q ^ 1

print(q)