# Codeup_Python 기초4-2.중첩반복문_1677: 종이 자르기

n,m = map(int, input("길이를 입력하세요: ").split())
for i in range(m):
    if i==0 or i==m-1:
        print('+'+'-'*(n-2)+'+')
    else:
        print('|'+' '*(n-2)+'|')


# 아니면 이렇게 미리 상단, 중간, 하단을 나누어서 미리 만들어둔다음 불러오는 식으로 코드를 짤 수도 있다. 
n, m = map(int, input("길이를 입력하세요: ").split())
t = '+' + '-' * (n - 2) + '+'
g = '|' + ' ' * (n - 2) + '|'
r = [t] + [g] * (m - 2) + [t]
print(r)
for i in r:
    print(i)