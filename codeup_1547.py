# Codeup_Python 기초100제_1547: 함수로 prime/composite 판별하기

import sys
def f(n):
    a = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a = False
            break
    print('prime' if a else 'composite')
n = int(sys.stdin.readline())
f(n)