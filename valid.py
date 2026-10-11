def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

print(is_valid("{[()]}"))
print(is_valid("([)]"))