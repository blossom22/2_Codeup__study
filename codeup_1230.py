# Codeup_Python 기초3.if~else_1230: 터널 통과하기 2

a=list(map(int, input("정수 3개를 입력하세요: ").split()))
for i in range(3):
    if a[i]<=170:
        print("CRASH",a[i])
        break
if min(a)>170:
    print("PASS")
