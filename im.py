from bisect import bisect_left

def lis_length(nums):
    tails = []

    for num in nums:
        i = bisect_left(tails, num)

        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num

    return len(tails)


print(lis_length([10, 9, 2, 5, 3, 7, 101, 18]))