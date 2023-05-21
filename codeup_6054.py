# Codeup_Python 기초100제_6054: 둘 다 참일 경우만 참 출력하기
a, b = map(int, input("정수 2개를 입력하세요: ").split())
print(bool(a) and bool(b))  # 여기서 and는 교집합 개념이다. or는 합집합 개념
