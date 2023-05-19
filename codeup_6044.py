# Codeup_Python 기초100제_6044: 정수 2개 입력받아 자동 계산하기
# 단, 나눈 값을 계산할때, 소수점 둘째자리까지만 나오도록 한다. 

a, b = map(int, input("정수 2개를 입력하세요: ").split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a/b, ".2f")) 

