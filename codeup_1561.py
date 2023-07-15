# Codeup_Python 기초100제_1561: 함수로 두 정수의 큰 값 리턴하기

import sys
def f(n):
    print(n) if n>m else print(m)
n,m = map(int, sys.stdin.readline().split())
f(n)

# max함수로 해결한 풀이
import sys
def f(n):
    print(max(n,m))
n,m = map(int, sys.stdin.readline().split())
f(n)