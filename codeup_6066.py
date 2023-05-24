# Codeup_Python 기초100제_6066: 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
d = [a, b, c]
for i in range(len(d)):
    if d[i] % 2 == 0:
        print("even")
    else:
        print("odd")