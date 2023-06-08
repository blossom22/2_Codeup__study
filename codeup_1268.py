# Codeup_Python 기초3.단순 반복문_1268: n개의 수 중 홀수의 개수

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
b=[i for i in a if i%2==1]
print(len(b))