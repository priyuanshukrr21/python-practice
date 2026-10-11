from collections import Counter

def first_unique(s):
    freq = Counter(s)

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None

print(first_unique("aabbcde"))