# Codeup_Python 기초100제_6093: 이상한 출석 번호 부르기2
n = int(input("출석번호를 부른 횟수를 입력하세요: "))
a = input("무작위로 부른 n개의 번호를 입력하세요: ").split()
for i in range(n):
    a[i] = int(a[i])    # 입력된 a리스트안의 값들을 정수로 바꾸는 과정

for i in range(n-1, -1, -1):    # 0까지 내림차순으로 가고싶으면 가운데 들어갈 수는 -1이다. 
    print(a[i], end=' ')
