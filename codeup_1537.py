# Codeup_Python 기초100제_1537: 함수로 hello 또는 world 출력하기

n = int(input())
def f(n):
    print('hello') if n == 1 else print('world')
f(n)


# sys모듈을 활용했다.
import sys
def f(n):
    print('hello') if n == 1 else print('world')
n = int(sys.stdin.readline())
f(n)