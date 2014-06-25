import sys
import math

__author__ = 'Eric'

def num2code(num):
    num = int(num)
    code = ''
    thousands = math.floor(num / 1000)
    hundreds = math.floor((num % 1000) / 100)
    tens = math.floor((num % 100) / 10)
    ones = num % 10

    digits = [thousands, hundreds, tens, ones]
    map = ['m', 'c', 'x', 'i']

    for i in range(4):
        digit = digits[i]
        if digit > 0:
            if digit > 1:
                code += str(digit)
            code += map[i]

    return code


def code2num(code):
    num = 0
    code = str(code).lower()
    letters = [['m', 1000], ['c', 100], ['x', 10], ['i', 1]]

    for pair in letters:
        index = code.find(pair[0])
        val = 0
        if index > -1:
            if index == 0 or code[index - 1].isalpha():
                val = 1
            else:
                val = int(code[index - 1])
            num += val * pair[1]

    return num

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x, y = sys.stdin.readline().split()
        x, y = code2num(x), code2num(y)
        print(num2code(x + y))

if __name__ == '__main__':
    main()