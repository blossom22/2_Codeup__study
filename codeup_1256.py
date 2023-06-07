# Codeup_Python 기초3.if~else_1256: 별 출력하기
n = int(input("개수를 입력하세요: "))
for i in range(n):
    print("*",end='')

# 아래처럼 for문을 한줄로 만들수도 있다. 
n = int(input("개수를 입력하세요: "))
a = list(range(n))
for i in a: print("*",end='')