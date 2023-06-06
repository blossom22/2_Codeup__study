# Codeup_Python 기초3.if~else_1253: a 부터 b까지 출력하기

# abs를 쓰지않고 if문안에 for문을 넣을 수 있다. 
a,b=map(int, input("두 수를 입력하세요: ").split())
if a>b:
    for i in range(a-b+1):
        print(b+i, end=' ')
else:
    for i in range(b-a+1):
        print(a+i, end=' ')


# 아니면 아래처럼 abs를 사용하여, for문안에 if문을 넣을 수 있다. 
# 그러나 이 방법은 코드길이는 위의 것보다 짧아도 코드실행시간측면에서 손해였다. 
a,b=map(int, input("두 수를 입력하세요: ").split())
for i in range(abs(a-b)+1):
    if a>b:
        print(b+i, end=' ')
    else:
        print(a+i, end=' ')

