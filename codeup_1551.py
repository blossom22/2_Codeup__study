# Codeup_Python 기초100제_1551: 함수로 원하는 값의 위치 리턴하기 1

import sys
def f(n,a,k):
    print(a.index(k)+1) if k in a else print(-1)
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
f(n,a,k)