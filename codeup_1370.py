# Codeup_Python 기초4-2.중첩반복문_1370: 지그재그 출력하기

h,r = map(int, input("정보를 입력하세요: ").split())
for i in range(r):
    for j in range(h):
        print(' '*j+'*')
        if j==h-1:
            for k in range(h-2,-1,-1):
                print(' '*k+'*')


# 아래는 위의 코드를 조금더 간결하게 만든 버전이다. 
h, r = map(int, input("정보를 입력하세요: ").split())
for i in range(r):
    for j in range(h):
        print(' ' * j + '*')
    for k in range(h - 2, -1, -1):
        print(' ' * k + '*')