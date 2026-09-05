arr = [10, 45, 23, 67, 34, 89]

largest = arr[0]
second = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]

print("Largest =", largest)
print("Second Largest =", second)