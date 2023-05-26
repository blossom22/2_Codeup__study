# Codeup_Python 기초100제_6087: 3의 배수는 통과
a = int(input("정수를 입력하세요: "))
for i in range(1, a+1):
    if i % 3 == 0:
        print("", end="")
    else:
        print(i, end=" ")



# 아니면 continue를 써서도 해결가능하다.
a = int(input("정수를 입력하세요: "))

for i in range(1, a+1) : 
    if i % 3 == 0 : 
        continue            # if 조건문 충족시 바로 다음단계로 넘어간다. 
    print(i, end=' ')  