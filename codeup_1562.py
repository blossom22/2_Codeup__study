# Codeup_Python 기초100제_1562: 함수로 두 정수의 작은 값 리턴하기

import sys
def f(n):
    print(m) if n>m else print(n)
n,m = map(int, sys.stdin.readline().split())
f(n)

# min함수로 해결한 풀이
import sys
def f(n):
    print(min(n,m))
n,m = map(int, sys.stdin.readline().split())
f(n)