# Codeup_Python 기초3.if~else_1162: 당신의 사주를 봐 드립니다 1

a, b, c = map(int, input("연월일을 입력하세요: ").split())
d = str(a - b + c)      # 슬라이싱하기위해 문자로 바꾸는 것
if d[-1] == "0":
    print("대박")
else:
    print("그럭저럭")