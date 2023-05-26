# Codeup_Python 기초100제_6086: 거기까지! 이제 그만~
a = int(input("정수를 입력하세요: "))
temp = 0
s = 0
while True:
    temp += 1
    s += temp
    if s >= a:
        break
print(s)
