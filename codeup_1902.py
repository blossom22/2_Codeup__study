# Codeup_Python 재귀함수_1902: (재귀 함수) 1부터 n까지 역순으로 출력하기

def f(n):
    print(n)
    n-=1
    if n>0: f(n)
n = int(input())
f(n)


# lambda를 이용한 풀이다. 
f=lambda n:(print(n),f(n-1)) if n>0 else None
n = int(input())
f(n)