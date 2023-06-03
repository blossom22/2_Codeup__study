# Codeup_Python 기초3.if~else_1180: 만능 휴지통

n = int(input("자연수를 입력하세요: "))
a = int(str(n)[1]+str(n)[0])
if (a*2)<100:
    if (a*2)<=50:
        print(a*2,"GOOD", sep="\n")
    else:
        print(a*2,"OH MY GOD", sep="\n")
else:                                       # a*2가 100이 넘는 경우(n은 문제조건에서 최대99이므로 100만 빼주면 된다)
    if (a*2-100) <=50:
        print(a*2-100,"GOOD", sep="\n")
    else:
        print(a*2-100,"OH MY GOD", sep="\n") 
