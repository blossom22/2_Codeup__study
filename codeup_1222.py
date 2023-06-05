# Codeup_Python 기초3.if~else_1222: 축구의 신 2

a,b,c = map(int, input("세 정수를 입력하세요: ").split())
b+=1
while True: 
    if a+5 < 90:
        b += 1
        a += 5
    else:
        break
print('win') if b>c else print('lose') if b<c else print('same')