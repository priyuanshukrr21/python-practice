import sys

print("Script:", sys.argv[0])

if len(sys.argv) > 1:
    print("Hello", sys.argv[1])
else:
    print("No name provided")