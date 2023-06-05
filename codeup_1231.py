# Codeup_Python 기초3.if~else_1231: 계산기 1

a = input("연산식을 입력하세요: ")
for i in range(len(a)):
    if a[i]=='+':
        print(int(a[:i]) + int(a[i+1:]))
    elif a[i]=='-':
        print(int(a[:i]) - int(a[i+1:]))
    elif a[i]=='*':
        print(int(a[:i]) * int(a[i+1:]))
    elif a[i]=='/':
        print(format(int(a[:i]) / int(a[i+1:]),".2f"))