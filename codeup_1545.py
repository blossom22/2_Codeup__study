# Codeup_Python 기초100제_1545: 함수로 true(1) / false(0) 리턴하기

import sys
def f(n):
    print('zero') if n==False else print('non zero')
n = int(sys.stdin.readline())
f(n)