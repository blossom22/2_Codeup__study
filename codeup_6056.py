# Codeup_Python 기초100제_6056: 참/거짓이 서로 다를 때에만 참 출력하기
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = bool(a)
d = bool(b)
print(c and (not d) or (not c) and d)

# 또는 아래처럼 if문으로 풀 수 있다. 
a, b = map(int, input("정수 2개를 입력하세요: ").split())
c = bool(a)
d = bool(b)
if c != d:
    print(True)
else:
    print(False)