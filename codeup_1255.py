# Codeup_Python 기초3.if~else_1255: 두 실수 사이 출력하기

a,b=map(float, input("실수를 입력하세요: ").split())  
while a<=b:                         # for문에서는 float을 증감변수로 사용하지 않아서 제약이 좀 있다. 
    print('%.2f'%a, end=' ')        # 소수점 둘째자리까지 출력하는 것 잊지말기
    a+=0.01                         # a를 소수점 둘째자리끼지 출력하고 0.01 더해줘. 그러다가 a가 b보다 커지면 while문 종료 