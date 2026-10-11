def rotate_array(nums, k):
    if not nums:
        return nums

    k %= len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))