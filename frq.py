text = input("Enter a string: ")

count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)