# Codeup_Python 기초3.if~else_1173: 30분전

a, b= map(int, input("시와 분을 입력하세요: ").split())
if a > 0:               # 30분전이 오늘인 경우
    if b >=30:
        print(a, b-30)
    else:
        print(a-1, b+30)
else:                   # 30분전이 전날인 경우
    if b >=30:
        print(a, b-30)
    else:
        print(23, b+30)