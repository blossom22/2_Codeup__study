# Codeup_Python 기초100제_6055: 하나라도 참이면 참 출력하기
a, b = map(int, input("정수 2개를 입력하세요: ").split())
print(bool(a) or bool(b)) 