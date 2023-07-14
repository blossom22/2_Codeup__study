# Codeup_Python 기초100제_1541: 함수로 negative/zero/positive 출력하기

import sys
def f(n):
    print('negative') if n<0 else print('positive') if n>0 else print('zero')
n = int(sys.stdin.readline())
f(n)