# Codeup_Python 기초4-2.중첩반복문_1358: 삼각형 출력하기 5

n = int(input("자연수를 입력하세요: "))
a=int(n/2)
for i in range(1,n+1,2):
    print(' '*a +'*'*i)
    a-=1

# 중첩반복문을 이용해보자. 
n = int(input("자연수를 입력하세요: "))
for i in range(1,n+1,2):
    for j in range((n - i) // 2):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()