# Codeup_Python 기초100제_1557: 함수로 n의 약수의 개수 리턴하기

def f(n):
    a=0
    for i in range(1,n+1):
        if n%i == 0:
            a+=1
    return a
n = int(input())
print(f(n))