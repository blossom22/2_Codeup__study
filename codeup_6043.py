# Codeup_Python 기초100제_6043: 실수 2개 입력받아 나눈 결과 계산하기
# 단, 소수점 셋째 자리까지 출력할 것
a, b = map(float, input("실수 2개를 입력하세요: ").split())
print(format(a/b, ".3f")) 

# 또는 round 함수를 써서 아래와 같이 해결할 수 있다. 
a, b = map(float, input("실수 2개를 입력하세요: ").split())
print(round(a/b, 3))   