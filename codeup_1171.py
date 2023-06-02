# Codeup_Python 기초3.if~else_1171: 당신의 학번은? 2

a, b, c = map(str, input("학년, 반, 번호를 입력하세요: ").split())
print(a+b.zfill(2)+c.zfill(3))