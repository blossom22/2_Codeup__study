# Codeup_Python 기초4-2.중첩반복문_1354: 삼각형 출력하기 2

n = int(input("자연수를 입력하세요: "))
for i in range(n,0,-1):
    print('*'*i)

# 아래는 join함수로 푼 방식이다. 
n = int(input("자연수를 입력하세요: "))
print('\n'.join('*'*i for i in range(n,0,-1)))