# Codeup_Python 기초100제_6088: 수 나열하기1
# 문제: 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가 공백을 두고 입력되면, n번째 수의 값을 출력해라. 

a, d, n = map(int, input("정수 3개를 입력하세요: ").split()) 
result = a+d*(n-1)      # 단순한 등차수열이다. 
print(result)
