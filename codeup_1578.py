# Codeup_Python 기초100제_1578: (함수 작성) 최댓값 함수

import sys
def f(a,b):
    print(max(a,b))
a,b = map(int, sys.stdin.readline().split())
f(a,b)


# max함수 없이 if문으로도 해결가능하다.
import sys
def f(a,b):
    print(a) if a>b else print(b)
a,b = map(int, sys.stdin.readline().split())
f(a,b)