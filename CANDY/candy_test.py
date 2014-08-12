from candy import *

__author__ = 'Eric'

def main():
    fail = 0

    cases = []
    cases.append([[1,1,1,1,6], 4])
    cases.append([[3,4], - 1])
    cases.append([[2,2,2], 0])
    cases.append([[1,7], 3])
    cases.append([[5], 0])

    for case in cases:
        result = move(case[0])
        if result != case[1]:
            print('MOVE FAILURE: Got {0}; Expected {1}'.format(result, case[1]))
            fail += 1

    if fail == 0:
        print('Yay!  No test failures!')
    else:
        print(str(fail) + ' total failures :(')

if __name__ == '__main__':
    main()
