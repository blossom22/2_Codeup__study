# Codeup_Python 기초4-2.중첩반복문_1368: 평행사변형 출력하기 2

h,k,d = input("정보를 입력하세요: ").split()
h=int(h)
k=int(k)
s ='*'*k
if d=='R':
    for i in range(h-1,-1,-1):
        print(' '*i+s)
else:
    for i in range(h):
        print(' '*i+s)
