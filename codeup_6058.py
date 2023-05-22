# Codeup_Python 기초100제_6058: 둘 다 거짓일 경우만 참 출력하기
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = bool(a)
d = bool(b)
print((not c) and (not d))