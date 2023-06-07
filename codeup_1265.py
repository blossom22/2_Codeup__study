# Codeup_Python 기초3.if~else_1265: 구구단 출력하기 1

n=int(input("자연수를 입력하세요: "))
for i in range(1,10):
    print("%d*%d=%d" %(n,i,n*i))

# 아래처럼 f-string을 사용하여 해결할 수도 있다. 
n = int(input())
for i in range(1, 10):
    print(f"{n}*{i}={n * i}")   
    
# f-string은   f'문자열{변수}문자열'   의 꼴을 하고 있다. 위에서 쓴 %로 표현하는 방식은 어떤 type인지도 지정(%s, %d..)해야해서 f-string에 비해서 귀찮다.
# 직관적이라는 장점외에도, 다른 이점들이 있다. f-string을 먼저 작성하고 나중에 변수를 말해줘도 알아먹고, 코드 실행시간도 단축시켜준다. 
# 다만, 변수명이 많이 길어지면 가독성이 떨어지는 단점이 있다. 