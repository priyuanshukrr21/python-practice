def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        required = target - num

        if required in seen:
            return [seen[required], i]

        seen[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))