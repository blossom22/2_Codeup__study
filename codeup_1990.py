# Codeup_Python 기초5-2.문자열_1990: 3의 배수 판별하기

n=int(input())
if n%3==0:
    print(1)
else:
    print(0)


# 아니면 아래처럼 간결하게 쓸수도 있다. 
[print(1) if int(input())%3==0 else print(0)]