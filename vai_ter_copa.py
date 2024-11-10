import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
