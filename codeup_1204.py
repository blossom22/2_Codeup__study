# Codeup_Python 기초3.if~else_1204: 영어 서수로 표현하기

a = int(input("정수를 입력하세요: "))
b = str(a).zfill(2)
if (11<=a<=13):
    print(a,"th",sep="")
else: 
    if b[1]=="1":
        print(a,"st",sep="")
    elif b[1]=="2":
        print(a,"nd",sep="")
    elif b[1]=="3":
        print(a,"rd",sep="")
    else:
        print(a,"th",sep="")
