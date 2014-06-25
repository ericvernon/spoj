from nsystem import *

__author__ = 'Eric'

def main():
    fail = 0

    cases = []
    cases.append([1, 'i'])
    cases.append([10, 'x'])
    cases.append([100, 'c'])
    cases.append([1000, 'm'])
    cases.append([7, '7i'])
    cases.append([81, '8xi'])
    cases.append([902, '9c2i'])
    cases.append([5004, '5m4i'])
    cases.append([8765, '8m7c6x5i'])
    cases.append([9999, '9m9c9x9i'])

    for case in cases:
        result = num2code(case[0])
        if result != case[1]:
            print('NUM2CODE FAILURE: Case {0}; Got {1}; Expected {2}'.format(case[0], result, case[1]))
            fail = 1

    for case in cases:
        result = code2num(case[1])
        if result != case[0]:
            print('CODE2NUM FAILURE: Case {0}; Got {1}; Expected {2}'.format(case[1], result, case[0]))
            fail = 1

    if fail == 0:
        print('Yay!  No test failures!')

if __name__ == '__main__':
    main()
