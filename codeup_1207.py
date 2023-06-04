# Codeup_Python 기초3.if~else_1207: 윷놀이

a=list(map(int, input("윷상태를 입력하세요: ").split()))
b=a.count(1)
if b==0:
    print("모")
elif b==1:
    print("도")
elif b==2:
    print("개")
elif b==3:
    print("걸")
else:
    print("윷")