import sys

__author__ = 'Eric'

def reverse(number):
    """Convert a number to its reversed form"""
    number = str(number)
    number = number[::-1]
    return int(number)

n = int(sys.stdin.readline())
for i in range(n):
    x, y = sys.stdin.readline().split()
    x, y = reverse(x), reverse(y)
    print(reverse(x + y))