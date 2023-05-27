# Codeup_Python 기초100제_6091: 함께 문제 푸는 날
# 문제: 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다. 이때, 3명이 다시 모두 함께 방문해 문제를 풀어보는 날을 구해라
a, b, c = map(int, input("정수 3개를 입력하세요: ").split()) 
day = 1
while day % a!=0 or day % b!=0 or day % c!=0 :  # while조건문 밖으로 나가려면, day값을 a, b, c로 나눴을때 나머지가 전부 0(공통배수)이어야 한다.
    day += 1
print(day) 

# 아니면 아래처럼 풀수도 있다.
a, b, c = map(int, input("정수 3개를 입력하세요: ").split()) 
for i in range(max(a,b,c), (a*b*c)+1):      # 최소공배수는 주어진 수들의 '공통배수' 중 '가장 작은 수'를 구하는 것이다.
    if i%a==0 and i%b==0 and i%c==0:
        print(i)
        break

