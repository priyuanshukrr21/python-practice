def missing_number(nums, n):
    expected = n * (n + 1) // 2
    return expected - sum(nums)

print(missing_number([1, 2, 4, 5], 5))