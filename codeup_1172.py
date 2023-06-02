# Codeup_Python 기초3.if~else_1172: 세 수 정렬하기

# 1. sort() 이용해서 정렬하는 방법
a = list(map(int, input("정수 3개를 입력하세요: ").split()))
a.sort()
for i in a:
    print(i, end = " ")

# 2. 직접 하나하나 비교해서 정렬하는 방식
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)  