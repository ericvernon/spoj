import sys

__author__ = 'Eric'

for line in sys.stdin:
    if int(line) == 42:
        break
    print(line)
