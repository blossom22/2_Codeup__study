# Codeup_Python 기초100제_6085: 그림 파일 저장용량 계산하기
r, g, b = map(int, input("정수 3개를 입력하세요: ").split())
temp = r*g*b/8/1024/1024
print('{:.2f}'.format(round(temp,2)), end=' MB')


# print(round(temp, 2), end=' MB') 6084번 문제처럼 그냥 이렇게 하면 안된다. 소수점아래 두자리를 반드시 표현해야는데, 이렇게 하면 소수점아래에 0이 있는 경우 둘째자리까지 표현되지 않는다. 