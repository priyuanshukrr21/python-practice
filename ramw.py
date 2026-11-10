import re

text = "Python 3.12!"

print(re.findall(r"\d", text))
print(re.findall(r"\D", text))
print(re.findall(r"\w", text))