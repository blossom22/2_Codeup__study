# Codeup_Python 기초100제_6089: 수 나열하기2
# 문제: 시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력되면, n번째 수가 출력되게 해라.

a, r, n = map(int, input("정수 3개를 입력하세요: ").split()) 
result = a*(r**(n-1))      # 단순한 등비수열이다. 
print(result)

