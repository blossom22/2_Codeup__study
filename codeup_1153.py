# Codeup_Python 기초3.if~else_1153: 두 수의 대소 비교

a, b = map(int, input("정수 2개를 입력하세요: ").split())
if a > b:
    print(">")
elif b > a:
    print("<")
else:
    print("=")