# Codeup_Python 기초100제_1556: 함수로 n! 리턴하기

def f(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a
n = int(input())
print(f(n))


# 재귀적으로 푸는 방법도 가능하다
def f(n):
    if n == 0 or n == 1:    # 0!이나 1!은 1이니까
        return 1
    else:
        return n * f(n-1)   # n! = n*(n-1)*(n-2)*....*1 이다. 즉 n*f(n-1)과 같다
n = int(input())
print(f(n))


# 람다함수(함수를 쓸때 매우 간략하게 해줌)를 이용하는 방법도 있다
# 람다함수는 기본적으로 "lambda 매개변수:표현식"의 꼴이다.
f=lambda n:1 if n<2 else n*f(n-1)   # 위에서 푼것처럼 재귀적으로 해결했다.   
print(f(int(input())))