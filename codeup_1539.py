# Codeup_Python 기초100제_1539: 함수로 false 또는 true 출력하기

import sys
def f(n):
    print('false') if n==0 else print('true')
n = int(sys.stdin.readline())
f(n)