# Codeup_Python 기초100제_6094: 이상한 출석 번호 부르기3
# 부른 n개의 번호 중 최소값을 출력해라.

# 아래처럼 그냥 min함수를 쓰면 편하다. 
n = int(input("출석번호를 부른 횟수를 입력하세요: "))
a = input("무작위로 부른 n개의 번호를 입력하세요: ").split()
for i in range(n):
    a[i] = int(a[i])    # 입력된 a리스트안의 값들을 정수로 바꾸는 과정
print(min(a))

# 아니면, a리스트 값들을 하나하나 비교하는 방법도 있다.
n = int(input("출석번호를 부른 횟수를 입력하세요: "))
a = input("무작위로 부른 n개의 번호를 입력하세요: ").split()
for i in range(n):
    a[i] = int(a[i])    
m = a[0]
for i in range(n):
    if a[i] < m:
        m = a[i]
print(m)