# Codeup_Python 기초3.if~else_1257: 두 수 사이의 홀수 출력하기

a,b=map(int, input("두 수를 입력하세요: ").split()) 
if a%2==1:
    while a<=b:
        print(a,end=' ')
        a+=2
else:
    while a<b:              # a가 짝수일때 이 줄에서 a<=b조건이면 b를 초과한 홀수가 출력되므로, a<b여야한다. 
        print(a+1,end=' ')
        a+=2
