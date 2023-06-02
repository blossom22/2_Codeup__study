# Codeup_Python 기초3.if~else_1168: 나이 계산 1

a, b = map(int, input("생년월일과 성별정보를 입력하세요: ").split())
c = str(a)      
d = c.zfill(6)      # zfill()은 인자로 전달된 숫자보다 문자열의 길이가 작을 때, 작은 크기만큼 앞 부분을 0으로 채운다. 이과정이 필요한 이유는 내가 입력한 a가 0으로 시작될 경우 0을 자동으로 지워버리기 때문이다.

if (b==1) or (b==2):
    print(2012 - int("19"+d[:2]) + 1)
else:
    print(2012 - int("20"+d[:2]) + 1)
