# Codeup_Python 기초100제_6025: 정수 2개 입력받아 합 계산하기
a, b = input("정수 2개를 입력하세요: ").split()
c = int(a) + int(b)     # 입력되는 것들은 기본적으로 다 문자취급이다. 그래서 int함수로 정수로 바꾸는 과정이 필요하다. 
print(c)