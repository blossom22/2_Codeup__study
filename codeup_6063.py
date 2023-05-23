# Codeup_Python 기초100제_6063: 정수 2개 입력받아 큰 값 출력하기
# 단, 3항 연산을 사용해서 풀어라. 
# 3항연산이란? '참인경우 값' if '조건' else '거짓인경우 값' ...이런식으로 구성된다.
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = a if (a>=b) else b
print(c)