# Codeup_Python 기초3.if~else_1163: 당신의 사주를 봐 드립니다 2

a, b, c = map(int, input("연월일을 입력하세요: ").split())
d = str(a + b + c)[-3]
if int(d) % 2 == 0:
    print("대박")
else:
    print("그럭저럭")