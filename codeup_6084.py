# Codeup_Python 기초100제_6084: 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input("정수 4개를 입력하세요: ").split())
temp = h*b*c*s/8/1024/1024
print(round(temp, 1), end=' MB')    # round함수로 원하는 소수점자리수를 표현할 수 있다. 