# Codeup_Python 기초3.if~else_1154: 큰수 - 작은수

a, b = map(int, input("정수 2개를 입력하세요: ").split())
print(abs(a-b))

# 아니면 문제의 취지에 맞게 if~else문으로 풀어보면 아래와 같다.
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = a - b
if c < 0:
    print(-c)
else:
    print(c)