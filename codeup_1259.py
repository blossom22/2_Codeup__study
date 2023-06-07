# Codeup_Python 기초3.if~else_1259: 1부터 n까지 중 짝수의 합 구하기
n=int(input("자연수를 입력하세요: "))
a=0
for i in range(1,n+1):
    if i%2==0: 
        a+=i
print(a)
