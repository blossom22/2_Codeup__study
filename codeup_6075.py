# Codeup_Python 기초100제_6075: 정수 1개 입력받아 그 수까지 출력하기1
# 0부터 그 수까지 줄을 바꿔 한 개씩 출력시켜라
a = int(input("정수를 입력하세요: "))
temp = 0
while temp <= a:
    print(temp)
    temp = temp + 1     # temp += 1 로 더 간결하게 쓸 수 있다. 
