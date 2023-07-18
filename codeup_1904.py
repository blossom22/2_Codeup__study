# Codeup_Python 재귀함수_1904: 두 수 사이의 홀수 출력하기
import sys
sys.setrecursionlimit(10**6)
def f(a,b):
    if b >= a:
        if a%2==0:
            f(a+1,b)
        else:
            print(a)
            f(a+2,b)
a,b = map(int, sys.stdin.readline().split())
f(a,b)