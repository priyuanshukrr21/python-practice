def merge_intervals(intervals):
    intervals.sort()
    merged = []

    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))