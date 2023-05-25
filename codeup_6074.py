# Codeup_Python 기초100제_6074: 문자 1개 입력받아 알파벳 출력하기
# 영문자 1개를 입력하면, a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력시켜라. 

# chr랑 ord함수를 이용하면 된다. 
# chr()는 정수값을 문자로 바꿔준다. ord()와는 반대의 기능을 한다.
k = ord(input("문자를 입력하세요: "))
temp = ord('a')
while temp <= k:
    print(chr(temp), end=' ')
    temp = temp + 1
