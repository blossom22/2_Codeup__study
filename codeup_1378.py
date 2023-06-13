# Codeup_Python 기초4-2.중첩반복문_1378: 수열의 합

n = int(input("자연수를 입력하세요: "))
a=[1]
b=1
for i in range(2,n+1):
    for j in [i]:
        b+=i
    a.append(b)
print(sum(a))
