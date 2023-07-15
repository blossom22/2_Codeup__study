# Codeup_Python 기초100제_1553: 함수로 정수 올림 한 값 리턴하기

import math
def f(n):
    print(math.ceil(n))     # 내장함수 round는 반올림, math모듈안의 ceil은 올림, floor은 내림, 소수점 그냥버림은 trunc 
n = float(input())
f(n)