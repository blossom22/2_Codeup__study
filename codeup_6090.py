# Codeup_Python 기초100제_6090: 수 나열하기3
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력되면, n번째 수를 출력해라. 

a, m, d, n = map(int, input("정수 4개를 입력하세요: ").split()) 
for i in range(2,n+1):
    a = a * m + d
print(a)