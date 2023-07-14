# Codeup_Python 기초100제_1535: 함수로 가장 큰 값 위치 리턴하기

n=int(input())
a=list(map(int,input().split()))
def f(): 
    print(a.index(max(a))+1)
f()