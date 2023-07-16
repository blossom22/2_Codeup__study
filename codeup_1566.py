# Codeup_Python 기초100제_1566: 함수로 거듭제곱 리턴하기

import sys
def f(a,b):
    print(a**b)
a,b = map(int, sys.stdin.readline().split())
f(a,b)


# pow 함수로 풀수도 있다. 주의할 점은 math모듈의 pow는 항상 float결과를 반환한다는 것이다. 따라서 정수타입을 원하면 내장함수 pow를 써야한다
import sys
def f(a,b):
    print(pow(a,b))
a,b = map(int, sys.stdin.readline().split())
f(a,b)

# lambda를 써봤다
f=lambda a,b:print(a**b)
a,b=map(int,input().split())
f(a,b)