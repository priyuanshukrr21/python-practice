
def find_median(nums1, nums2):
    a, b = nums1, nums2

    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)

    if m + n == 0:
        raise ValueError("Arrays cannot both be empty")

    left_size = (m + n + 1) // 2
    low, high = 0, m

    while low <= high:
        i = (low + high) // 2
        j = left_size - i

        a_left = float("-inf") if i == 0 else a[i - 1]
        a_right = float("inf") if i == m else a[i]
        b_left = float("-inf") if j == 0 else b[j - 1]
        b_right = float("inf") if j == n else b[j]

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return max(a_left, b_left)

            return (
                max(a_left, b_left) +
                min(a_right, b_right)
            ) / 2

        elif a_left > b_right:
            high = i - 1
        else:
            low = i + 1

    raise ValueError("Input arrays must be sorted")


print(find_median([1, 3], [2]))
print(find_median([1, 2], [3, 4]))
