# Codeup_Python 기초100제_1563: 함수로 세 정수 중 중간 값 리턴하기

import sys
def f(n):
    n.sort()
    print(n[1])
n = list(map(int, sys.stdin.readline().split()))
f(n)


# 아니면 리스트를 정렬할 필요없이, 그냥 최소값을 지운 리스트에서의 최소값을 구하면 된다
def f(n):
    n.remove(min(n))
    print(min(n))
f(list(map(int,input().split())))