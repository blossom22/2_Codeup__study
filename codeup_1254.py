# Codeup_Python 기초3.if~else_1254: 알파벳 출력하기

a,b=map(ord, input("알파벳을 입력하세요: ").split())        # ord()함수는 특정 문자의 유니코드 정수를 반환한다. 
for i in range(b-a+1):
    print(chr(a+i),end=' ')                                # chr()함수는 특정 정수의 유니코드 문자를 반환한다. 