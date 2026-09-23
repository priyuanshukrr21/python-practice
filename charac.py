def first_non_repeating(s):
    frequency = {}

    # Count frequency of each character
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Find the first character with frequency 1
    for char in s:
        if frequency[char] == 1:
            return char

    return None


s = "aabbcddee"

result = first_non_repeating(s)

print(result)