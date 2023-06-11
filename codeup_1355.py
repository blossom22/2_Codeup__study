# Codeup_Python 기초4-2.중첩반복문_1355: 삼각형 출력하기 3

n = int(input("자연수를 입력하세요: "))
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i)

# 아래의 코드는 중첩반복문을 이용해보았다.
n = int(input("자연수를 입력하세요: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()