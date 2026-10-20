
from bisect import bisect_left

def lis_length(nums):
    tails = []

    for x in nums:
        i = bisect_left(tails, x)

        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x

    return len(tails)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_length(nums))
