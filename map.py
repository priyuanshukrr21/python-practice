a, b = map(int, input().split())

result = 1

for i in range(b):
    result *= a

print(result)