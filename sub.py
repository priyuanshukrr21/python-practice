def max_subarray(nums):
    current = best = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)

    return best

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))