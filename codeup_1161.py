# Codeup_Python 기초3.if~else_1161: 홀수와 짝수 그리고 더하기

a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = a + b

if a % 2 == 0:
    print('짝수+',end='')
else:
    print('홀수+',end='')
if b % 2 == 0:
    print('짝수=',end='')
else:
    print('홀수=',end='')
if c % 2 == 0:
    print('짝수')
else:
    print('홀수')

