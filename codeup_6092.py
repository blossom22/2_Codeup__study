# Codeup_Python 기초100제_6092: 이상한 출석 번호 부르기1

n = int(input("출석번호를 부른 횟수를 입력하세요: "))
a = input("무작위로 부른 n개의 번호를 입력하세요: ").split()
for i in range(n):
    a[i] = int(a[i])    # 입력된 a리스트안의 값들을 정수로 바꾸는 과정

data = []
for j in range(23):
    data.append(0)

for i in range(n):
    data[a[i]-1] += 1     # a리스트안의 값들이 적힌만큼 data리스트에서 1씩 더하는 과정 (1을빼는 과정이 있는이유는 data에서 인덱스값때문이다)
for i in range(23):
    print(data[i], end = ' ')
