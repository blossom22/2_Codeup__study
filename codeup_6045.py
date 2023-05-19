# Codeup_Python 기초100제_6045: 정수 3개 입력받아 합과 평균 출력하기
# 단, 평균의 경우 소수점아래 둘째자리까지 출력할 것
a, b, c= map(int, input("정수 3개를 입력하세요: ").split())
s = a + b + c
print(s, format(s/3, ".2f"))

# 마지막 줄을 이런식으로도 쓸 수 있다. 
print(s, '%.2f' %(s/3))