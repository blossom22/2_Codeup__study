# Codeup_Python 기초3.if~else_1165: 축구의 신 1

a, b = map(int, input("현재 경기시간과 우리팀의 득점을 입력하세요: ").split())
c = 1
while True: 
    if a+5 < 90:
        c += 1
        a += 5
    else:
        break
print(b+c)

