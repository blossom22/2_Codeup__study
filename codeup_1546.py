# Codeup_Python 기초100제_1546: 함수로 plus/minus/0 판별하기

import sys
def f(n):
    print('zero') if n==0 else print('plus') if n>0 else print('minus')
n = int(sys.stdin.readline())
f(n)
