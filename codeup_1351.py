# Codeup_Python 기초4-2.중첩반복문_1351: 구구단 출력하기 2

a, b= map(int, input("수를 입력하세요: ").split())
for i in range(a,b+1):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")

