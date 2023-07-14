# Codeup_Python 기초100제_1543: 함수로 love 출력하기

def f(n):
    for i in range(n):
        print('love')
n = int(input())
f(n)


# 이또한 sys 모듈사용할 수 있다. 
import sys
def f(n):
    for _ in range(n):
        print('love')
n = int(sys.stdin.readline())
f(n)