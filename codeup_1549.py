# Codeup_Python 기초100제_1549: 함수로 절댓값 리턴하기

def f(n):
    print(abs(n))
n = int(input())
f(n)

# abs()를 쓰지 않고 이런 풀이도 가능하다
def f(n):
    print(n*(n>0)-n*(n<0))      # n>0 이면 True. True는 정수값1로 평가되고, False는 정수값0으로 평가된다.
n = int(input())
f(n)