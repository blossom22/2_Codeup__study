# Codeup_Python 기초100제_6078: 원하는 문자가 입력될 때까지 반복 출력하기
# 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력시켜라

while True:         # 무한루프 만들고.
    a = input()
    print(a)        # 'q'출력될때까지 입력한 문자 출력
    if a == 'q':
        break       # 'q'출력되면 while문 빠져나와

