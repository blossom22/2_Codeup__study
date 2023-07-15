# Codeup_Python 기초100제_1550: 함수의 양의 제곱근의 정수 부분만 리턴하기

import sys, math
def f(n):
    print(math.trunc(n**(1/2)))     # math모듈의 trunc()함수는 소수점아래의 수들을 전부 버린다. math.floor()과 다른점은 floor의 경우, 소수점을 버리면서 더 낮은 정수로 내림을 하지만, trunc는 단순히 소수점아래 수만 버릴뿐이다
n = int(sys.stdin.readline())
f(n)


# math모듈에서 isqrt() 함수 쓰는 방법도 있다.
# isqrt()는 제곱근을 계산하고 정수부분만 반환해준다. 
import math
def f(n):
    print(math.isqrt(n))
n = int(input())
f(n)