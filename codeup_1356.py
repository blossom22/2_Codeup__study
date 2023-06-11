# Codeup_Python 기초4-2.중첩반복문_1356: 사각형 출력하기 2

n = int(input("자연수를 입력하세요: "))
for i in range(n):
    if i == 0 or i == n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
