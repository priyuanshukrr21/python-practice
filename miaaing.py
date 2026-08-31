numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2
sum_numbers = 0

for num in numbers:
    sum_numbers += num

missing = total - sum_numbers

print("Missing Number:", missing)