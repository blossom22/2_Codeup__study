# Codeup_Python 기초100제_1544: 함수로 * n개 출력하기

import sys
def f(n):
    print('*'*n)
n = int(sys.stdin.readline())
f(n)


# sys모듈 사용안한 풀이
def f(n):
    print('*'*n)
n = int(input())
f(n)