# Codeup_Python 기초3.if~else_1170: 당신의 학번은? 1

a, b, c = map(int, input("학년, 반, 번호를 입력하세요: ").split())
if c < 10:
    d = "0"+str(c)
else:
    d = str(c)
print(str(a)+str(b)+d)
