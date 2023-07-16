# Codeup_Python 기초100제_1567: 함수로 배열의 부분합 리턴하기

import sys
def f(a,b):
    print(sum(k[a-1:b]))
n = int(input())
k = list(map(int, sys.stdin.readline().split()))
a,b = map(int, sys.stdin.readline().split())
f(a,b)

