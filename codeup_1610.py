# Codeup_Python 기초100제_1610: 서브 스트링

import sys
def f(a, b, c):
    print(a[b:b+c])
a = input()
b, c = map(int, sys.stdin.readline().split())
f(a, b, c)