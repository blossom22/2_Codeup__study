# Codeup_Python 기초3.if~else_1261: First Special Judge (Test)

a=list(map(int, input("두 수를 입력하세요: ").split()))
b=0
for i in range(10):
    if a[i]%5==0:
        print(a[i])
        break           # 5의 배수 하나만 출력하라고 했으므로, 답을 찾으면 바로 if문 break시켜
    else:
        b+=1            # 5의 배수 아닌 것을 카운트한것이 b
        if b==10:
            print(0)