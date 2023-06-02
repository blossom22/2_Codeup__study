# Codeup_Python 기초3.if~else_1170: 당신의 학번은? 1

a, b, c = map(int, input("학년, 반, 번호를 입력하세요: ").split())
if c < 10:
    d = "0"+str(c)
else:
    d = str(c)
print(str(a)+str(b)+d)

# 아니면 그냥 zfill()로 간결하게 표현가능하다.
a, b, c = map(str, input("학년, 반, 번호를 입력하세요: ").split())
d = c.zfill(2)
print(a+b+d)