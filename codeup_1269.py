# Codeup_Python 기초3.단순 반복문_1269: 수열의 값 구하기

a,b,c,n=map(int, input("수를 입력하세요: ").split())
for i in range(2,n+1):
    a=a*b+c
print(a)