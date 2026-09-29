arr = list(map(int, input().split()))

current = 1
maximum = 1

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        current += 1
    else:
        current = 1

    maximum = max(maximum, current)

print("Length =", maximum)