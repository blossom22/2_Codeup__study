# Codeup_Python 재귀함수_1912: (재귀 함수) 팩토리얼 계산
import sys
sys.setrecursionlimit(10**6)
def f(n,a):
    if n>0:
        a *=n
        f(n-1,a)
    else:
        print(a)
n = int(input())
f(n,a=1)