# Codeup_Python 기초3.if~else_1218: 삼각형 판단하기

a,b,c = map(int, input("변의길이를 입력하세요: ").split())
if c<a+b:
    if a==b==c:
        print("정삼각형")
    elif a==b or b==c or a==c:
        print("이등변삼각형")
    elif a**2 + b**2 == c**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")