# Codeup_Python 기초3.if~else_1216: 컨설팅 회사

a,b,c = map(int, input("입력하세요: ").split())
print("advertise") if (b-c)>a else print("do not advertise") if (b-c)<a else print("does not matter")   # if~elif~else문도 이렇게 한줄로 표현가능하다.

