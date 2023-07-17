# Codeup_Python 재귀함수_1901: (재귀 함수) 1부터 n까지 출력하기

def f(n,i=1):
    print(i)
    if i < n: f(n,i+1)
n = int(input())
f(n)

# lambda를 이용해보았다.
f=lambda n,i=1:i<=n and(print(i),f(n,i+1))      # 만약 i>n이면 False가 되므로 and뒤에 있는 코드 실행하지 않는다.
n=int(input())
f(n)
# 위의 코드를 이렇게도 쓸수있다
f=lambda n,i=1:(print(i),f(n,i+1)) if i<=n else None   
n=int(input())
f(n)