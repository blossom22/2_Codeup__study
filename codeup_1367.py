# Codeup_Python 기초4-2.중첩반복문_1367: 평행사변형 출력하기 1

n = int(input("크기를 입력하세요: "))
s ='*'*n 
for i in range(n-1,-1,-1):
    print(' '*i+s)

