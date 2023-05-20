# Codeup_Python 기초100제_6047: 2의 거듭제곱 배로 곱해 출력하기
# 정수 2개(a,b)를 입력받아, a와 2의b제곱을 곱한 값을 출력해라

a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = a * (2 ** b)
print(c)

# 또는 6046번에서 풀었듯이, 비트시프트연산을 하면된다.
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = a<<b    # a를 2**b를 곱한 값을 c에 저장한다. 
print(c)
