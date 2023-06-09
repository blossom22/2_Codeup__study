# Codeup_Python 기초3.단순 반복문_1282: 제곱수 만들기

n=int(input("수를 입력하세요: "))
t=int(n**(1/2))     # 이렇게하면 n의제곱근의 소수부분을 버린 정수부분만 출력한다. 
k=n-t**2
print(k,t)

# 출제자의 의도에 맞게 반복문을 써보자. 
n=int(input("수를 입력하세요: "))
k=0
t=1
while n>=(t**2):
    t+=1
print(n-(t-1)**2, t-1)