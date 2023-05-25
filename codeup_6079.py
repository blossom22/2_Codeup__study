# Codeup_Python 기초100제_6079: 언제까지 더해야 할까?

temp = 0
s = 0
a = int(input("정수를 입력하세요: "))
while True:
    if a > s :
        temp += 1
        s += temp
    else:
        break
print(temp)
