# Codeup_Python 기초3.if~else_1164: 터널 통과하기 1

a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
if (a <= 170) or (b <= 170) or (c <= 170) :
    print("CRASH")
else:
    print("PASS")

# 아니면 min함수로 조금 더 간결하게 표현가능하다. 
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
if min (a,b,c) <=170:
    print("CRASH")
else:
    print("PASS")
