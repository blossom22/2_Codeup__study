# Codeup_Python 기초3.if~else_1260: 3의 배수의 합

a,b=map(int, input("두 수를 입력하세요: ").split())
c=0
while a<=b:
    if a%3==0:
        c+=a
    a+=1
print(c)