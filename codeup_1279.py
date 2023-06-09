# Codeup_Python 기초3.단순 반복문_1279: 홀수는 더하고 짝수는 빼고 1

a, b=map(int, input("두 자연수를 입력하세요: ").split())
c=0
for i in range(a,b+1):
    if i % 2 == 1:  # 홀수인 경우
        c += i
    else:           # 짝수인 경우
        c -= i
print(c)