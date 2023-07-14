# Codeup_Python 기초100제_1548: 함수로 학점 리턴하기

import sys
def f(n):
    if n>=90:
        print('A')
    elif n>=80:
        print('B')
    elif n>=70:
        print('C')
    elif n>=60:
        print('D')
    else:
        print('F')
n = int(sys.stdin.readline())
f(n)