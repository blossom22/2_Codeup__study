# Codeup_Python 기초100제_6077: 짝수 합 구하기
# 정수 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
a = int(input("정수를 입력하세요: "))
temp = 0
for i in range(1,a+1):
    if i%2 == 0:
        temp += i
print(temp)

