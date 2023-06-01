# Codeup_Python 기초3.if~else_1166: 윤년 판별

a = int(input("자연수를 입력하세요: "))
if (a % 400 == 0) or ((a % 4==0) and (a % 100!=0)):
    print("Leap")
else:
    print("Normal")