# Codeup_Python 기초100제_1579: (함수 작성) 최솟값 함수

import sys
def f(a,b):
    print(min(a,b))
a,b = map(int, sys.stdin.readline().split())
f(a,b)


# max함수 없이 if문으로도 해결가능하다.
import sys
def f(a,b):
    print(b) if a>b else print(a)
a,b = map(int, sys.stdin.readline().split())
f(a,b)


# lambda를 이용한 풀이
f = lambda a, b: a if a < b else b
a, b = map(int, input().split())
print(f(a, b))