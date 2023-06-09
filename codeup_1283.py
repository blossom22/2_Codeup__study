# Codeup_Python 기초3.단순 반복문_1283: 주식 투자

a=int(input("투자금액을 입력하세요: "))
b=int(input("투자일수를 입력하세요: "))
c=list(map(int, input("변동폭을 입력하세요: ").split()))
d=a
for i in range(b):
    a+=a*c[i]/100
print(round(a-d))
if round(a-d)>0:
    print('good')
elif round(a-d)<0:
    print('bad')
else:
    print('same')


