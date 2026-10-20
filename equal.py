
def two_sum_pairs(nums, target):
    seen = set()
    pairs = set()

    for x in nums:
        complement = target - x

        if complement in seen:
            pairs.add(tuple(sorted((x, complement))))

        seen.add(x)

    return sorted(pairs)


nums = [1, 5, 7, -1, 5]
print(two_sum_pairs(nums, 6))
