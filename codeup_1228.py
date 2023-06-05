# Codeup_Python 기초3.if~else_1228: 비만도 측정 1

a,b=map(float, input("키와 몸무게를 입력하세요: ").split())
c=(a-100)*0.9
d=(b-c)*100/c
print("정상") if d<=10 else print("비만") if d>20 else print("과체중")
