# Codeup_Python 기초100제_1538: 함수로 odd 또는 even 출력하기

import sys
def f(n):
    print('odd') if n%2==1 else print('even')
n = int(sys.stdin.readline())
f(n)