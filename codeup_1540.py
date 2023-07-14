# Codeup_Python 기초100제_1540: 함수로 zero 또는 non zero 출력하기

import sys
def f(n):
    print('zero') if n==0 else print('non zero')
n = int(sys.stdin.readline())
f(n)